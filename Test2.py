import scipy.stats as stats
import numpy as np
import pandas as pd

df = pd.read_csv(r"assets/NISPUF17.csv", index_col=0)
df = df[["HAD_CPOX","P_NUMVRC"]]

print(df)