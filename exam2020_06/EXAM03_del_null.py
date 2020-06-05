import numpy as np
import pandas as pd
data = pd.DataFrame(pd.read_excel("del_col.xlsx"))
# data_not_null = data[data['准牵引质量'
#                           '燃料种类',
#                           '车宽',
#                           '车高',
#                           '轴数',
#                           '轴距',
#                           '轮胎规格',
#                           '轮胎数',
#                           '总质量',
#                           '装备质量',
#                           '核定载质量',
#                           '核定载客',
#                           '准牵引质量',
#                           '底盘企业',
#                           '底盘品牌',
#                           '底盘型号',
#                           '年龄',
#                           '性别'
# ].notna()]
#一旦所在列有空的值，就删除所在行
data_not_null = data.dropna(subset=['准牵引质量',
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
print('删除前形状',data.shape)
print('删除后形状',data_not_null.shape)
data_not_null.to_excel("del_null.xlsx")
print('finish')