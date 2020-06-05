#删除没用的列，如厢长，厢宽，厢高这三列
import numpy as np
import pandas as pd
data = pd.DataFrame(pd.read_excel("del_re.xlsx"))
data2 = data.drop(["厢长","厢宽","厢高"],axis=1)
data2.to_excel("del_col.xlsx")
print('finish')