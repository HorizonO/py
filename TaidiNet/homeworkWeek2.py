# 国民数据可视化：
# # 1.文件读取及数据查看
# # 2.绘制2000年第一季度各产业国民生产总值分布直方图
# # 3.绘制2000年第一季度各产业国民生产总值分布饼图
# # 4.绘制2000-2017年各产业国民生产总值箱线图
import numpy as np
import matplotlib.pyplot as plt
data = np.load('E:/国民经济核算季度数据/国民经济核算季度数据.npz')
a=data.files
data = np.loadtxt('E:/国民经济核算季度数据/国民经济核算季度数据.npz')

#1.直方图

