from sklearn.datasets import  load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import numpy as np
# import pandas as pd
# data =pd.read_excel('new_Cars_Data.xlsx')
# # result_dic = data.groupby('brand')['count'].apply(int).to_dict()
# dataList = data['车辆名称牌'].value_counts()
# print(dataList)
# # dataList.to_csv("品牌统计.csv")
# # print(result_dic)


#聚类分析
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans #导入kmeans算法
airline_scale = np.load('../tmp/airline_scale.npz')['arr_0']
k = 5 ## 确定聚类中心数
#构建模型
kmeans_model = KMeans(n_clusters = k,n_jobs=4,random_state=123)
fit_kmeans = kmeans_model.fit(airline_scale)   #模型训练
kmeans_model.cluster_centers_ #查看聚类中心

kmeans_model.labels_ #查看样本的类别标签

#统计不同类别样本的数目
r1 = pd.Series(kmeans_model.labels_).value_counts()
print('最终每个类别的数目为：\n',r1)