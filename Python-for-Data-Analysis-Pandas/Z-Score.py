import numpy as np
import pandas as pd

x = pd. Series ( [2.1, 2.3, 4.5, 2.2, 2.4])
mean = np.mean(x)
std = np.std(x)
outliers = []
for item in x:
    z_score = (item - mean) / std
    if z_score > 1.5:
     outliers.append(item)
print (outliers)