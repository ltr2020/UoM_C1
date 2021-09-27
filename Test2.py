import scipy.stats as stats
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\NISPUF17.csv", index_col=0)
df = df[["HAD_CPOX","P_NUMVRC"]].dropna()
df = df[df["HAD_CPOX"]<=2].dropna()
print(df["HAD_CPOX"].unique())
print(df["P_NUMVRC"].unique())
corr, pval = stats.pearsonr(df["HAD_CPOX"],df["P_NUMVRC"])
return corr
