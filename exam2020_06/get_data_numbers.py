import pandas as pd
import xlrd
import numpy as np
# col=['排量','功率','车长','车高','车宽','轴数','轴距','总质量','整备质量','核定载客','年龄']
# data = pd.read_excel('new_Cars_Data.xlsx',index_col=0,usecols=col)
# print(df)
# df.to_csv('模型数据.csv')

data = pd.read_csv('模型数据.csv')
feature = ['功率','车长','车高','车宽','轴数','轴距','总质量','整备质量','核定载客','年龄']
data_mean = data.mean()   #平均
data_std = data.std()  #标准化
print(type(data),type(data_mean),type(data_std))
# data_train = (data - data_mean)/data_std
# print(data_train)