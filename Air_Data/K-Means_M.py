# from Air_Data import make_LRFMC_M
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
airline_scale = np.load("airline_scale.npz")['arr_0']
k = 5
kmeans_model = KMeans(n_clusters=k,n_jobs=4,random_state=123)
fit_kmeans = kmeans_model.fit(airline_scale)
kmeans_model.cluster_centers_
kmeans_model.labels_
r1 = pd.Series(kmeans_model.labels_).value_counts()
print(r1)