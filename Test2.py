import pandas as pd
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 10)
    import numpy as np
    df = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\NISPUF17.csv", index_col=0)
    df = df.loc[:, ["CBF_01", "P_NUMFLU"]]
