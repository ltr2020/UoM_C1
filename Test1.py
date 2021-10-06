import math

import pandas as pd
import numpy as np
data = {"class" : ["fruit", "fruit", "vegetable", "vegetable", "vegetable"],
                  "avg" : [95, 202, 164, math.nan, 207]}
df = pd.DataFrame(data, index=["apple", "mango", "potato", "onion", "broccoli"])
print(df)
print(df.groupby("class",axis=0))
print(df.groupby(["class", "avg"]))
print(df.groupby("class"))