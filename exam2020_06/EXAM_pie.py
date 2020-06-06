import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("new_Cars_Data.xlsx")
cars_selection = data[["市"]]
# print(cars_selection)
Data_list = cars_selection#str
Data_list.to_excel("Data_list.xlsx")
# resoult = {}
# print(Data_list)
# for i in Data_list:
#     resoult[i] = Data_list.count(i)
# print(resoult)


