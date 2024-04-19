code = """
import numpy as np

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection, metrics
from sklearn.model_selection import KFold

from sklearn.preprocessing import QuantileTransformer


qt = QuantileTransformer(n_quantiles=80, output_distribution='normal')

features = np.ones([100, 100])
# 按方差或最终效果剔除某些特征 78 -6 =72
remove_features = [0, 2, 20, 24, 44, 76]
features = np.delete(features, remove_features, axis=1)

# 这里用QuantileTransformer来进行scaling
features = qt.fit_transform(features)

mean = features.mean()
std = features.std()
# 简单归一化
features = (features - mean) / std

labels = np.ones(100)


def create_models():
    # Randomforest
    rf = RandomForestClassifier(n_estimators=1000,
                                criterion='entropy',
                                max_features=25,
                                bootstrap=True,
                                random_state=42,
                                warm_start=False,
                                class_weight=None,
                                n_jobs=-1,
                                )
    # XGBoost
    xgb = XGBClassifier(
        n_estimators=1000,
        booster='gbtree',
        max_depth=10,
        #objective = 'binary:logistic',
        reg_lambda=1,
        subsample=0.5,
        gamma=0.5,
        colsample_bytree=0.75,
        min_child_weight=2,
        learning_rate=0.25,
        n_jobs=-1,
        random_state=42
    )
    # lightGBM
    lgbm = LGBMClassifier(
        max_depth=5,
        learning_rate=0.1,
        n_estimators=1000,
        objective='binary',
        subsample=0.8,
        n_jobs=-1,
        num_leaves=30,
        colsample_bytree=0.75,
        random_state=42
    )
    # catboost
    cat = CatBoostClassifier(
        iterations=1000,
        learning_rate=0.1,
        max_depth=7,
        verbose=100,
        task_type='CPU',
        eval_metric='AUC',
        random_state=42,
        thread_count=-1,
    )

    return rf, xgb, lgbm, cat


xSample = features
ySample = labels

rf_preds_all = []
xgb_preds_all = []
lgbm_preds_all = []
cat_preds_all = []

metrics_dict = {"rf": {}, "xgb": {}, "lgbm": {}, "cat": {}}
for model in metrics_dict.keys():
    metrics_dict[model] = {"AUC": 0.0, "ACC": 0.0, "Recall": 0.0, "F1-score": 0.0, "Precesion": 0.0}


N_splits = 5
kf = KFold(n_splits=N_splits)

num = 0
for train_index, valid_index in kf.split(xSample):

    train_X, train_y = xSample[train_index], ySample[train_index]
    valid_X, valid_y = xSample[valid_index], ySample[valid_index]

    rf, xgb, lgbm, cat = create_models()

    rf.fit(train_X, train_y)
    xgb.fit(train_X, train_y)
    lgbm.fit(train_X, train_y)
    cat.fit(train_X, train_y)

    rf_preds = rf.predict_proba(valid_X)[:, 1]
    xgb_preds = xgb.predict_proba(valid_X)[:, 1]
    lgbm_preds = lgbm.predict_proba(valid_X)[:, 1]
    cat_preds = cat.predict_proba(valid_X)[:, 1]

    rf_preds_all.append(rf_preds)
    xgb_preds_all.append(xgb_preds)
    lgbm_preds_all.append(lgbm_preds)
    cat_preds_all.append(cat_preds)

    rf_pred_labels = (rf_preds >= 0.5) * 1
    xgb_pred_labels = (xgb_preds >= 0.5) * 1
    lgbm_pred_labels = (lgbm_preds >= 0.5) * 1
    cat_pred_labels = (cat_preds >= 0.5) * 1

    for model in metrics_dict.keys():
        metrics_dict[model]["AUC"] += metrics.roc_auc_score(valid_y, eval(f'{model}_pred_labels')) / N_splits
        metrics_dict[model]["ACC"] += metrics.accuracy_score(valid_y, eval(f'{model}_pred_labels')) / N_splits
        metrics_dict[model]["Recall"] += metrics.recall_score(valid_y, eval(f'{model}_pred_labels')) / N_splits
        metrics_dict[model]["F1-score"] += metrics.f1_score(valid_y, eval(f'{model}_pred_labels')) / N_splits
        metrics_dict[model]["Precesion"] += metrics.precision_score(valid_y, eval(f'{model}_pred_labels')) / N_splits

    num = num + 1

"""
