import numpy as py
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel("new_Cars_Data.xlsx")
sex = data['性别'].value_counts()

values = [1020,477]
labels = ['男性','女性']
plt.bar(labels,values,width=0.5)
# labels = ['五菱','长安','北京','东风','奥路卡','松花江','金杯','开瑞','江铃全顺','大马','其他']
# values = [907, 260, 177, 55, 42, 22, 17, 5, 3, 3, 6]
plt.bar(labels,values,width=0.5,color='skyblue')
plt.xlabel('性别')
# plt.xlabel('品牌')
plt.ylabel('数量')
plt.title('男女性别对比')
# plt.title('汽车品牌数量直方图')
# plt.savefig('汽车品牌数量直方图.jpg')
plt.show()
print('07陈旭霖')