import numpy as np
import pandas as pd

x = pd. Series ( [2.1, 2.3, 4.5, 2.2, 2.4])
median = np.median(x)
threshold = 2
outliers  = []
for item in x :
      if (item - median) > threshold:
       outliers.append(item)
print (outliers)