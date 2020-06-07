
import numpy as np
import pandas as pd
cars_data = pd.read_excel("new_Cars_Data.xlsx",encoding="utf-8") #导数据
print('原始数据的形状为：',cars_data.shape)
## 选取需求特征
cars_selection = cars_data[['功率','车长','车高','车宽','轴数','轴距','总质量','整备质量','核定载客','年龄']]
## 构建L特征
L = pd.to_datetime(cars_selection["年龄"]) - \
pd.to_datetime(cars_selection["年龄"])
L = L.astype("str").str.split().str[0]
L = L.astype("int")/30
## 合并特征
cars_features = pd.concat([L,
    cars_selection.iloc[:,2:]],axis = 1)
print('构建的LRFMC特征前5行为：\n',cars_selection.head())

from sklearn.preprocessing import StandardScaler
data = StandardScaler().fit_transform(cars_selection)
np.savez('cars.npz',data)
print('标准化后五个特征为：\n',data[:5,:])

