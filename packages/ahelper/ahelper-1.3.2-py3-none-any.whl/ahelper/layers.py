# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import math
import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
from torch.nn import ModuleList, Linear, BatchNorm1d, Identity


def init_model_params(module, n_layers):
    if isinstance(module, nn.Linear):
        module.weight.data.normal_(mean=0.0, std=0.02 / math.sqrt(n_layers))
        if module.bias is not None:
            module.bias.data.zero_()
    if isinstance(module, nn.Embedding):
        module.weight.data.normal_(mean=0.0, std=0.02)


def softplus_inverse(x):
    return x + np.log(-np.expm1(-x))


class RBFLayer(nn.Module):
    def __init__(self, K=64, cutoff=10, dtype=torch.float):
        super().__init__()
        self.cutoff = cutoff

        centers = torch.tensor(softplus_inverse(np.linspace(1.0, np.exp(-cutoff), K)), dtype=dtype)
        self.centers = nn.Parameter(F.softplus(centers))

        widths = torch.tensor([softplus_inverse(0.5 / ((1.0 - np.exp(-cutoff) / K)) ** 2)] * K, dtype=dtype)
        self.widths = nn.Parameter(F.softplus(widths))

    def cutoff_fn(self, D):
        x = D / self.cutoff
        x3, x4, x5 = torch.pow(x, 3.0), torch.pow(x, 4.0), torch.pow(x, 5.0)
        return torch.where(x < 1, 1 - 6 * x5 + 15 * x4 - 10 * x3, torch.zeros_like(x))

    def forward(self, D):
        D = D.unsqueeze(-1)
        return self.cutoff_fn(D) * torch.exp(-self.widths * torch.pow((torch.exp(-D) - self.centers), 2))


class MLP(nn.Module):
    def __init__(self, hidden_size, ffn_size, dropout_rate):
        super(MLP, self).__init__()

        self.layer1 = nn.Linear(hidden_size, ffn_size)
        self.gelu = nn.GELU()
        self.layer2 = nn.Linear(ffn_size, hidden_size)

    def forward(self, x):
        x = self.layer1(x)
        x = self.gelu(x)
        x = self.layer2(x)
        return x


class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_size, attention_dropout_rate, head_size):
        super(MultiHeadAttention, self).__init__()

        self.head_size = head_size

        self.att_size = att_size = hidden_size // head_size
        self.scale = att_size ** -0.5

        self.linear_q = nn.Linear(hidden_size, head_size * att_size)
        self.linear_k = nn.Linear(hidden_size, head_size * att_size)
        self.linear_v = nn.Linear(hidden_size, head_size * att_size)
        self.att_dropout = nn.Dropout(attention_dropout_rate)

        self.output_layer = nn.Linear(head_size * att_size, hidden_size)

    def forward(self, q, k, v, attn_bias=None):
        orig_q_size = q.size()

        d_k = self.att_size
        d_v = self.att_size
        batch_size = q.size(0)

        # head_i = Attention(Q(W^Q)_i, K(W^K)_i, V(W^V)_i)
        q = self.linear_q(q).view(batch_size, -1, self.head_size, d_k)
        k = self.linear_k(k).view(batch_size, -1, self.head_size, d_k)
        v = self.linear_v(v).view(batch_size, -1, self.head_size, d_v)

        q = q.transpose(1, 2)                  # [b, h, q_len, d_k]
        v = v.transpose(1, 2)                  # [b, h, v_len, d_v]
        k = k.transpose(1, 2).transpose(2, 3)  # [b, h, d_k, k_len]

        # Scaled Dot-Product Attention.
        # Attention(Q, K, V) = softmax((QK^T)/sqrt(d_k))V
        q = q * self.scale
        x = torch.matmul(q, k)  # [b, h, q_len, k_len]
        if attn_bias is not None:
            x = x + attn_bias

        x = torch.softmax(x, dim=3)
        x = self.att_dropout(x)
        x = x.matmul(v)  # [b, h, q_len, attn]

        x = x.transpose(1, 2).contiguous()  # [b, q_len, h, attn]
        x = x.view(batch_size, -1, self.head_size * d_v)

        x = self.output_layer(x)

        assert x.size() == orig_q_size
        return x


class EncoderLayer(nn.Module):
    def __init__(self, hidden_size, ffn_size, dropout_rate, attention_dropout_rate, head_size):
        super(EncoderLayer, self).__init__()

        self.self_attention_norm = nn.LayerNorm(hidden_size)
        self.self_attention = MultiHeadAttention(hidden_size, attention_dropout_rate, head_size)
        self.self_attention_dropout = nn.Dropout(dropout_rate)

        self.ffn_norm = nn.LayerNorm(hidden_size)
        self.ffn = MLP(hidden_size, ffn_size, dropout_rate)
        self.ffn_dropout = nn.Dropout(dropout_rate)

    def forward(self, x, attn_bias=None):
        y = self.self_attention_norm(x)
        y = self.self_attention(y, y, y, attn_bias)
        y = self.self_attention_dropout(y)
        x = x + y

        y = self.ffn_norm(x)
        y = self.ffn(y)
        y = self.ffn_dropout(y)
        x = x + y
        return x


class JumpingKnowledge(torch.nn.Module):

    def __init__(self, mode):
        super(JumpingKnowledge, self).__init__()
        self.mode = mode.lower()
        assert self.mode in ['c', 's', 'm', 'l']

    def forward(self, xs):
        assert isinstance(xs, list) or isinstance(xs, tuple)

        if self.mode == 'c':
            return torch.cat(xs, dim=-1)
        elif self.mode == 's':
            nr = 0
            for x in xs:
                nr += x
            return nr
        elif self.mode == 'm':
            return torch.stack(xs, dim=-1).max(dim=-1)[0]
        elif self.mode == 'l':
            return xs[-1]

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.mode)


class MLP(torch.nn.Module):
    def __init__(self, in_channels: int, hidden_channels: int,
                 out_channels: int, num_layers: int, dropout: float = 0.0,
                 batch_norm: bool = True, relu_first: bool = False):
        super(MLP, self).__init__()

        self.lins = ModuleList()
        self.lins.append(Linear(in_channels, hidden_channels))
        for _ in range(num_layers - 2):
            self.lins.append(Linear(hidden_channels, hidden_channels))
        self.lins.append(Linear(hidden_channels, out_channels))

        self.batch_norms = ModuleList()
        for _ in range(num_layers - 1):
            norm = BatchNorm1d(hidden_channels) if batch_norm else Identity()
            self.batch_norms.append(norm)

        self.dropout = dropout
        self.relu_first = relu_first

    def reset_parameters(self):
        for lin in self.lins:
            lin.reset_parameters()
        for batch_norm in self.batch_norms:
            batch_norm.reset_parameters()

    def forward(self, x):
        for lin, batch_norm in zip(self.lins[:-1], self.batch_norms):
            x = lin(x)
            if self.relu_first:
                x = batch_norm(x.relu_())
            else:
                x = batch_norm(x).relu_()
            x = F.dropout(x, p=self.dropout, training=self.training)
        x = self.lins[-1](x)
        return x


class SIGN(torch.nn.Module):
    def __init__(self, in_channels: int, hidden_channels: int,
                 out_channels: int, num_embeddings: int, num_layers: int,
                 dropout: float = 0.0, batch_norm: bool = True,
                 relu_first: bool = False):
        super(SIGN, self).__init__()

        self.mlps = ModuleList()
        for _ in range(num_embeddings):
            mlp = MLP(in_channels, hidden_channels, hidden_channels,
                      num_layers, dropout, batch_norm, relu_first)
            self.mlps.append(mlp)

        self.mlp = MLP(num_embeddings * hidden_channels, hidden_channels,
                       out_channels, num_layers, dropout, batch_norm,
                       relu_first)

    def reset_parameters(self):
        for mlp in self.mlps:
            mlp.reset_parameters()
        self.reset_parameters()

    def forward(self, xs):
        out = []
        for x, mlp in zip(xs, self.mlps):
            out.append(mlp(x))
        out = torch.cat(out, dim=-1).relu_()
        return self.mlp(out)


code = r"""
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import math
import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
from torch.nn import ModuleList, Linear, BatchNorm1d, Identity


def init_model_params(module, n_layers):
    if isinstance(module, nn.Linear):
        module.weight.data.normal_(mean=0.0, std=0.02 / math.sqrt(n_layers))
        if module.bias is not None:
            module.bias.data.zero_()
    if isinstance(module, nn.Embedding):
        module.weight.data.normal_(mean=0.0, std=0.02)


def softplus_inverse(x):
    return x + np.log(-np.expm1(-x))


class RBFLayer(nn.Module):
    def __init__(self, K=64, cutoff=10, dtype=torch.float):
        super().__init__()
        self.cutoff = cutoff

        centers = torch.tensor(softplus_inverse(np.linspace(1.0, np.exp(-cutoff), K)), dtype=dtype)
        self.centers = nn.Parameter(F.softplus(centers))

        widths = torch.tensor([softplus_inverse(0.5 / ((1.0 - np.exp(-cutoff) / K)) ** 2)] * K, dtype=dtype)
        self.widths = nn.Parameter(F.softplus(widths))

    def cutoff_fn(self, D):
        x = D / self.cutoff
        x3, x4, x5 = torch.pow(x, 3.0), torch.pow(x, 4.0), torch.pow(x, 5.0)
        return torch.where(x < 1, 1 - 6 * x5 + 15 * x4 - 10 * x3, torch.zeros_like(x))

    def forward(self, D):
        D = D.unsqueeze(-1)
        return self.cutoff_fn(D) * torch.exp(-self.widths * torch.pow((torch.exp(-D) - self.centers), 2))


class MLP(nn.Module):
    def __init__(self, hidden_size, ffn_size, dropout_rate):
        super(MLP, self).__init__()

        self.layer1 = nn.Linear(hidden_size, ffn_size)
        self.gelu = nn.GELU()
        self.layer2 = nn.Linear(ffn_size, hidden_size)

    def forward(self, x):
        x = self.layer1(x)
        x = self.gelu(x)
        x = self.layer2(x)
        return x


class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_size, attention_dropout_rate, head_size):
        super(MultiHeadAttention, self).__init__()

        self.head_size = head_size

        self.att_size = att_size = hidden_size // head_size
        self.scale = att_size ** -0.5

        self.linear_q = nn.Linear(hidden_size, head_size * att_size)
        self.linear_k = nn.Linear(hidden_size, head_size * att_size)
        self.linear_v = nn.Linear(hidden_size, head_size * att_size)
        self.att_dropout = nn.Dropout(attention_dropout_rate)

        self.output_layer = nn.Linear(head_size * att_size, hidden_size)

    def forward(self, q, k, v, attn_bias=None):
        orig_q_size = q.size()

        d_k = self.att_size
        d_v = self.att_size
        batch_size = q.size(0)

        # head_i = Attention(Q(W^Q)_i, K(W^K)_i, V(W^V)_i)
        q = self.linear_q(q).view(batch_size, -1, self.head_size, d_k)
        k = self.linear_k(k).view(batch_size, -1, self.head_size, d_k)
        v = self.linear_v(v).view(batch_size, -1, self.head_size, d_v)

        q = q.transpose(1, 2)                  # [b, h, q_len, d_k]
        v = v.transpose(1, 2)                  # [b, h, v_len, d_v]
        k = k.transpose(1, 2).transpose(2, 3)  # [b, h, d_k, k_len]

        # Scaled Dot-Product Attention.
        # Attention(Q, K, V) = softmax((QK^T)/sqrt(d_k))V
        q = q * self.scale
        x = torch.matmul(q, k)  # [b, h, q_len, k_len]
        if attn_bias is not None:
            x = x + attn_bias

        x = torch.softmax(x, dim=3)
        x = self.att_dropout(x)
        x = x.matmul(v)  # [b, h, q_len, attn]

        x = x.transpose(1, 2).contiguous()  # [b, q_len, h, attn]
        x = x.view(batch_size, -1, self.head_size * d_v)

        x = self.output_layer(x)

        assert x.size() == orig_q_size
        return x


class EncoderLayer(nn.Module):
    def __init__(self, hidden_size, ffn_size, dropout_rate, attention_dropout_rate, head_size):
        super(EncoderLayer, self).__init__()

        self.self_attention_norm = nn.LayerNorm(hidden_size)
        self.self_attention = MultiHeadAttention(hidden_size, attention_dropout_rate, head_size)
        self.self_attention_dropout = nn.Dropout(dropout_rate)

        self.ffn_norm = nn.LayerNorm(hidden_size)
        self.ffn = MLP(hidden_size, ffn_size, dropout_rate)
        self.ffn_dropout = nn.Dropout(dropout_rate)

    def forward(self, x, attn_bias=None):
        y = self.self_attention_norm(x)
        y = self.self_attention(y, y, y, attn_bias)
        y = self.self_attention_dropout(y)
        x = x + y

        y = self.ffn_norm(x)
        y = self.ffn(y)
        y = self.ffn_dropout(y)
        x = x + y
        return x


class JumpingKnowledge(torch.nn.Module):

    def __init__(self, mode):
        super(JumpingKnowledge, self).__init__()
        self.mode = mode.lower()
        assert self.mode in ['c', 's', 'm', 'l']

    def forward(self, xs):
        assert isinstance(xs, list) or isinstance(xs, tuple)

        if self.mode == 'c':
            return torch.cat(xs, dim=-1)
        elif self.mode == 's':
            nr = 0
            for x in xs:
                nr += x
            return nr
        elif self.mode == 'm':
            return torch.stack(xs, dim=-1).max(dim=-1)[0]
        elif self.mode == 'l':
            return xs[-1]

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.mode)


class MLP(torch.nn.Module):
    def __init__(self, in_channels: int, hidden_channels: int,
                 out_channels: int, num_layers: int, dropout: float = 0.0,
                 batch_norm: bool = True, relu_first: bool = False):
        super(MLP, self).__init__()

        self.lins = ModuleList()
        self.lins.append(Linear(in_channels, hidden_channels))
        for _ in range(num_layers - 2):
            self.lins.append(Linear(hidden_channels, hidden_channels))
        self.lins.append(Linear(hidden_channels, out_channels))

        self.batch_norms = ModuleList()
        for _ in range(num_layers - 1):
            norm = BatchNorm1d(hidden_channels) if batch_norm else Identity()
            self.batch_norms.append(norm)

        self.dropout = dropout
        self.relu_first = relu_first

    def reset_parameters(self):
        for lin in self.lins:
            lin.reset_parameters()
        for batch_norm in self.batch_norms:
            batch_norm.reset_parameters()

    def forward(self, x):
        for lin, batch_norm in zip(self.lins[:-1], self.batch_norms):
            x = lin(x)
            if self.relu_first:
                x = batch_norm(x.relu_())
            else:
                x = batch_norm(x).relu_()
            x = F.dropout(x, p=self.dropout, training=self.training)
        x = self.lins[-1](x)
        return x


class SIGN(torch.nn.Module):
    def __init__(self, in_channels: int, hidden_channels: int,
                 out_channels: int, num_embeddings: int, num_layers: int,
                 dropout: float = 0.0, batch_norm: bool = True,
                 relu_first: bool = False):
        super(SIGN, self).__init__()

        self.mlps = ModuleList()
        for _ in range(num_embeddings):
            mlp = MLP(in_channels, hidden_channels, hidden_channels,
                      num_layers, dropout, batch_norm, relu_first)
            self.mlps.append(mlp)

        self.mlp = MLP(num_embeddings * hidden_channels, hidden_channels,
                       out_channels, num_layers, dropout, batch_norm,
                       relu_first)

    def reset_parameters(self):
        for mlp in self.mlps:
            mlp.reset_parameters()
        self.reset_parameters()

    def forward(self, xs):
        out = []
        for x, mlp in zip(xs, self.mlps):
            out.append(mlp(x))
        out = torch.cat(out, dim=-1).relu_()
        return self.mlp(out)

"""
