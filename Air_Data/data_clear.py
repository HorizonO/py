import numpy as np
import pandas as pd
airline_data = pd.read_csv("Air_Data.csv",encoding="gb18030")
print("原始数据的形状：",airline_data.shape)
exp1 = airline_data["SUM_YR_1"].notnull()
exp2 = airline_data["SUM_YR_2"].notnull()

exp = exp1&exp2
airline_notnull = airline_data.loc[exp,:]
print("删除缺失数据后的形状：",airline_notnull.shape)

index1 = airline_notnull['SUM_YR_1'] !=0
index2 = airline_notnull['SUM_YR_2'] !=0
index3 = (airline_notnull['SEG_KM_SUM'] > 0) & (airline_notnull
                                                ['avg_discount']!=0)
airline = airline_notnull[(index1|index2)&index3]
print("删除异常记录后数据的形状为：",airline.shape)

