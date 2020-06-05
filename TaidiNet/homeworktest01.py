# 生成一百个二维坐标点，计算任意两点的距离
#基本思路：生成长度为100的二维数组，然后再计算每两点之间x（i）-x（j）的距离和y（i）-y（j)的距离，形成一个新的二维数组
import numpy as np
# x = np.arange(100).reshape(100,1)
x = np.random.randint(0,100,100).reshape(100,1)
y = np.random.randint(0,100,100).reshape(100,1)
# print(x)
# print(y)
Combine = np.hstack((x,y))      #横向合并，全部坐标100个
# print(Combine)
# 随便抽取两个坐标点（随机生成一个整数对应的下标）
one = np.random.randint(100)    #生成第一个随机数
print(Combine[one])             #随机数对应的下标的坐标
two = np.random.randint(100)    #生成第二个随机数
print(Combine[two])             #随机数对应的下标的坐标


Xdistance = int(Combine[one][0]-Combine[two][0])   #横坐标相减
Ydistance = int(Combine[one][1]-Combine[two][1])   #纵坐标相减
#两点之间直线距离求解公式   d = sqrt(（x1-x2)**2+(y1-y2)**2)  sqrt是开根号的意思
d = np.sqrt(Xdistance**2+Ydistance**2)
print('两点的距离为：'+str(d))