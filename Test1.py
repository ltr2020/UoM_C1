import pandas as pd
import numpy as np
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 12)

df = pd.read_csv(r'C:\Users\user\PycharmProjects\UoM_C1\Doc\census.csv')
def method_slow():
    for state in df["STNAME"].unique():
        avg = np.average(df[df["STNAME"]==state].dropna()["CENSUS2010POP"])
        return("Counties in state " + state + " have an avg pop of " + str(avg))

def method_fast():
    for group, frame in df.groupby("STNAME"):
        avg = np.average(frame["CENSUS2010POP"])
        return("Counties in state " + state + " have an avg pop of " + str(avg))
