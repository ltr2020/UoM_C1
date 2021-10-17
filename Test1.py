import pandas as pd
import numpy as np
import scipy.stats as stats
import re

nba_df = pd.read_csv("Doc/nba.csv")
nba_df = nba_df[~nba_df.SRS.str.contains("Divsion")]

