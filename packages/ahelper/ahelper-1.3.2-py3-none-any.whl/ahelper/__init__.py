from . import deepwalk, snn, feature, links, utils, layers

__all__ = ['deepwalk', 'snn', 'feature', 'links', 'utils', 'nlu_lora', 'medicalgpt']

desc = {'deepwalk': 'deepwalk that accept sp.csr_matrix',
        'snn': "spiking neurons",
        'feature': "feature engineering, xgboost, lightgbm, catboost, rf",
        'links': ' some links available during competition',
        'utils': 'lrscheduler, loss',
        'layers': 'layers'}


rename = """
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", nargs="?", default="ogb")
args = parser.parse_args()

fileList = os.listdir(str(args.name))

for i in fileList:
    # 设置旧文件名（就是路径+文件名）
    if not i.endswith('.txt'):
        continue
    oldname = os.path.join(str(args.name), i)

    newname = oldname[:-4]
    print(oldname, '======>', newname)
    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名

"""