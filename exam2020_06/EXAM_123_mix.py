import pandas as pd
#读取数据，并打印原始数据的形状，n行n列？？
data = pd.read_excel("Cars_SaleData.xlsx",encoding="utf-8")
print("原始数据形状:",data.shape)
#打印全部数据
# print(data)


# 缺失值与异常值处理
#第一步：删除表格中重复的行
re_row = data.duplicated()
# print("这一行是否重复了：",re_row)

#去除重复行后的数据，new_cars_data
new_cars_data = data.drop_duplicates()
print("去除重复行后的数据：",new_cars_data.shape)        #打印后，发现有三列没用的数据

#删除3列没用的数据（厢长，厢宽，厢高这三列）,得到data2
new_cars_data = pd.DataFrame(pd.read_excel("del_re.xlsx"))
data2 = new_cars_data.drop(["厢长","厢宽","厢高"],axis=1)
print("去除3列无用数据后的形状：",data2.shape)

#接下来是删除有空值的行，确保数据的完整性，易于分析
#data_not_null
data_not_null = data2.dropna(subset=['准牵引质量',
                                    '燃料种类',
                                    '车宽',
                                    '车高',
                                    '轴数',
                                    '轴距',
                                    '轮胎规格',
                                    '轮胎数',
                                    '总质量',
                                    '整备质量',
                                    '核定载质量',
                                    '核定载客',
                                    '准牵引质量',
                                    '底盘企业',
                                    '底盘品牌',
                                    '底盘型号',
                                    '年龄',
                                    '性别'])
print('删除前形状',data2.shape)
print('删除后形状',data_not_null.shape)
#把过滤后的数据写入一个名为new_Cars_Data.xlsx的文件里，用于之后的图形化分析，和模型构建
data_not_null.to_excel("new_Cars_Data.xlsx")
print("Finish! 07cxl")#个人标识