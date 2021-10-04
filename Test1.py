import pandas as pd
import numpy as np
df = pd.read_csv('Doc\census.csv')
for group, frame in df.groupby("STNAME"):
    print(frame)