
# coding: utf-8

# In[4]:

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os


# Any results you write to the current directory are saved as output.
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import roc_auc_score

import lightgbm as lgb

import matplotlib.pyplot as plt
#import seaborn as sns

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')


# In[5]:

random_state = 42
np.random.seed(random_state)
df_train = pd.read_table('totalExposureLog_count1_static_uniq_average_process.txt')
df_test = pd.read_csv('./Btest_sample_new_no_price.csv')


# In[6]:

df_test.head()


# In[7]:

# df_test1=df_test[['sample_id','id',  'time','material_size','ad_industry_id','product_id','ad_count_id', 'price','product_type']]
df_test1=df_test[['id',  'time','material_size','ad_industry_id','product_id','ad_count_id']]

# In[12]:

lgb_params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': {'mape'},# {'l2', 'rmse','mape'}
    'num_leaves': 50,##   由于lightGBM是leaves_wise生长，官方说法是要小于2^max_depth
     'max_depth': 10,# ###   根据问题来定咯，由于我的数据集不是很大，所以选择了一个适中的值，其实4-10都无所谓。
    'subsample': 0.8, 
    'colsample_bytree': 0.8, 
    'learning_rate': 0.1,
    'feature_fraction': 0.8, ##  特征采样
    'bagging_fraction': 0.8,##  数据采样
    'bagging_freq': 10,
    'verbose': 0
}


# In[13]:

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=random_state)
# print(df_train)
oof = df_train[['id', 'label']]
oof['predict'] = 0
predictions = df_test1[['id']]
val_mse = []
feature_importance_df = pd.DataFrame()
# df_test["price"]=math.log(df_test["price"])

# In[14]:

features = [col for col in df_train.columns if col not in ['label',"product_type","price",'sample_id',"id",'time']]
#'material_size',,'product_id',,'price',

X_test = df_test[features].values
# print(type(df_test))
# print(type(X_test))
print("df_train.mean() ")
print(df_train["label"].mean() )

from sklearn.metrics import mean_squared_error
for fold, (trn_idx, val_idx) in enumerate(skf.split(df_train, df_train['label'])):
    X_train, y_train = df_train.iloc[trn_idx][features], df_train.iloc[trn_idx]['label']
    X_valid, y_valid = df_train.iloc[val_idx][features], df_train.iloc[val_idx]['label']
    
    N =2
    p_valid,yp = 0,0
    for i in range(N):
#         X_t, y_t = augment(X_train.values, y_train.values)
#         y_t=np.array(y_train)
        y_t=y_train
#         print(y_train )
#         print(type(y_train ))
#         print(type(X_train ))
        X_t = pd.DataFrame(X_train)
    
    
        trn_data = lgb.Dataset(X_t, label=y_t)
        val_data = lgb.Dataset(X_valid, label=y_valid)
        evals_result = {}
        lgb_clf = lgb.train(lgb_params,
                        trn_data,
                        100000,
                        valid_sets = [trn_data, val_data],
                        early_stopping_rounds=3000,
                        verbose_eval = 1000,
                        evals_result=evals_result
                       )
        p_valid += lgb_clf.predict(X_valid)
       # print("p_valid")
       # print(p_valid)
        
        yp += lgb_clf.predict(X_test)
    fold_importance_df = pd.DataFrame()
    fold_importance_df["feature"] = features
    fold_importance_df["importance"] = lgb_clf.feature_importance()
    fold_importance_df["fold"] = fold + 1
    feature_importance_df = pd.concat([feature_importance_df, fold_importance_df], axis=0)
    oof['predict'][val_idx] = p_valid/N
    val_score=mean_squared_error(y_valid, p_valid) ** 0.5
    #val_score = roc_auc_score(y_valid, p_valid)
    val_mse.append(val_score)
    
    predictions['fold{}'.format(fold+1)] = yp/N


mean_mse = np.mean(val_mse)
std_mse = np.std(val_mse)
all_mse = mean_squared_error(oof['label'], oof['predict'])
print("Mean mse: %.9f, std mse: %.9f. All mse: %.9f." % (mean_mse, std_mse, all_mse))


cols = (feature_importance_df[["feature", "importance"]]
        .groupby("feature")
        .mean()
        .sort_values(by="importance", ascending=False)[:1000].index)
best_features = feature_importance_df.loc[feature_importance_df.feature.isin(cols)]
print("best_features")
print(best_features.sort_values(by="importance",ascending=False))
predictions['target'] = np.mean(predictions[[col for col in predictions.columns if col not in ['id', 'label']]].values, axis=1)
predictions.to_csv('lgb_all_predictions_no_price_01.csv', index=None)
sub_df = pd.DataFrame({'id':df_test['id'].values})
sub_df["target"] = predictions['target']
print("df_test.mean() ")
print(sub_df["target"].mean() )
sub_df.to_csv("lgb_submission_with_price_size_id_log_no_price_no_product_type.csv", index=False)


