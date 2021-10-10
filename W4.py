print("1: Basic Stats Testing")
import numpy as np
import pandas as pd
from scipy import stats
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)
df=pd.read_csv ('Doc/grades.csv')
print("There are {} rows and {} columns".format(df.shape[0], df.shape[1]))
# segment this population into two pieces
# Let's say those who finish the first assignment by the end of December 2015, we'll call them early finishers,
# and those who finish it sometime after that, we'll call them late finishers.

early_finishers= df[pd.to_datetime(df['assignment1_submission']) < '2016']
late_finishers1= df[pd.to_datetime(df['assignment1_submission']) >= '2016']
late_finishers2= df[~df.index.isin(early_finishers.index)]