import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(4,4))  #创建一个空画布，指定画布大小，像素

x  = np.arange(10)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.legend(['sin','cos'])   #名称
plt.title('lines')   #显示标题
plt.show()


data = np.load('E:/国民经济核算季度数据/国民经济核算季度数据.npz')
# data.files
# data['columns']
# data['values']
# plt.scatter(range(69),data['values'][:,2])
# plt.show()
