from Air_Data import data_clear
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
airline_selection = data_clear.airline[["FFP_DATE","LOAD_TIME","FLIGHT_COUNT","LAST_TO_END",
                             "avg_discount","SEG_KM_SUM"]]
L = pd.to_datetime(airline_selection["LOAD_TIME"])-pd.to_datetime(airline_selection["FFP_DATE"])
L = L.astype("str").str.split().str[0]
L = L.astype("int")/30
airline_features = pd.concat([L,airline_selection.iloc[:,2:]],axis=1)
print("构建LRFMC特征前5行为：\n",airline_features.head())

data = StandardScaler().fit_transform(airline_features)
np.savez("airline_scale.npz",data)
print("标准化后模型的5个特征：\n",data[:5,:])