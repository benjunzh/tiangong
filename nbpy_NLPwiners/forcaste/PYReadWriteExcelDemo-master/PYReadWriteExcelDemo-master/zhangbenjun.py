import pandas as pd
import numpy as np

csvdata = pd.read_csv('dataset.csv')
csvdata = csvdata.iloc[:, :].values
data = csvdata[:, 0:-1]
flag = csvdata[:, -1:]
result = []
for i in range(data.shape[0]):
    temp = data[i, np.array(np.nonzero(data[i]))]
    if temp.size > 0:
        result.append([temp.min(), flag[i, 0].tolist()])

print(result)