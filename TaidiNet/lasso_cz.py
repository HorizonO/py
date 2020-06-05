import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
inputFile = 'data.csv'
data = pd.read_csv(inputFile)
# print(data)

print(data.corr())