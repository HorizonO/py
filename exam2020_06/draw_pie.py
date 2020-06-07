import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
data = pd.read_excel("new_Cars_Data.xlsx")

dataList = data['品牌'].value_counts()
# print(dataList)
#把数据得出新的csv文件
# dataList.to_csv("品牌统计.csv")
# plt.figure(figsize=(6,6))

#series --> array
#dataList2 = np.array(dataList)

#读取 品牌统计.csv
# with open("品牌统计.csv",encoding="utf-8") as data_brand:
#     reader = csv.reader(data_brand)
#     print(reader)
#     #
#     # for row in reader:
#     #     print(row)
# def get_column():
#     with open("品牌统计.csv",encoding="utf-8") as brand:
#         reader = csv.reader(brand)
#         column1 = [row[0] for row in reader]
#         print(column1)
#     with open("品牌统计.csv", encoding="utf-8") as brand:
#         reader = csv.reader(brand)
#         column2 = [row[1] for row in reader]
#         print(column2)
#
# get_column()

#字典格式读取csv
# with open('品牌统计.csv',encoding="utf-8") as brand:
#     dict={}
#     reader = csv.DictReader(brand)
#     for row in reader:
#         print(row)

#读取新数据
df = pd.read_csv('品牌统计2.csv',index_col=0)
print(type(df))
#把汽车品牌和数量统计出来
result_dic = df.groupby('brand')['count'].apply(int).to_dict()
print(result_dic)
label = []
# print(result_dic['count'])

#转换为npz文件
# np.savez('brandCount',result_dic)
for key,value in result_dic.items():
    # print("\nkey: ",type(key))
    # print("Value:",type(value))

    label.append(key)
print(label)


#作图函数
def DrawPie():
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(8, 8))

    #不合并,复杂写法
    # labels = ['五菱','长安','北京','东风','奥路卡','松花江','金杯','开瑞','江铃全顺',
    #           '大马','柯斯达','依维柯','吉奥','大通','飞碟','力帆']
    # size = [907,260,177,55,42,22,17,5,3,3,1,1,1,1,1,1]
    # explodes = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

    #如果将后面6个数据合并为一个数据，写法：
    labels = ['五菱','长安','北京','东风','奥路卡','松花江','金杯','开瑞','江铃全顺','大马','其他']
    size = [907, 260, 177, 55, 42, 22, 17, 5, 3, 3, 6]
    explodes = [0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]
    plt.pie(size,labels=labels,autopct='%1.1f%%',startangle=150,explode=explodes)
    plt.title('汽车品牌使用比例（07cxl）')
    plt.savefig('汽车品牌统计饼图.jpg')
    plt.show()


DrawPie()
print('07陈旭霖')
# plt.figure(figsize=(8,8))
# label = []
# explode = [0.01]
# plt.pie(value,explode=explode,labels=label)
# plt.title('brand')
# plt.show()

# dictionary = df.groupby('brand')['count'].apply(lambda x:str(x)).to_dict()
# print(dictionary)

