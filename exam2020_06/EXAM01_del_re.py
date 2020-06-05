import numpy as np
import pandas as pd
data = pd.read_excel("Cars_SaleData.xlsx",encoding="utf-8")
print("原始数据形状:",data.shape)
# print(cars_sales)
# 缺失值与异常值处理

re_row = data.duplicated()
# print("这一行是否重复了：",re_row)

#去除重复行后的数据
new_cars_data = data.drop_duplicates()
print(new_cars_data)
new_cars_data.to_excel("del_re.xlsx")

