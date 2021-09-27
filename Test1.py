def proportion_of_education():
    import pandas as pd
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 10)
    import numpy as np
    df = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\NISPUF17.csv", index_col=0)
    n = len(df["EDUC1"])
    POE1 = (np.sum(df["EDUC1"] == 1)) / n
    POE2 = (np.sum(df["EDUC1"] == 2)) / n
    POE3 = (np.sum(df["EDUC1"] == 3)) / n
    POE4 = (np.sum(df["EDUC1"] == 4)) / n
    POE = {"less than high school": POE1,
           "high school": POE2,
           "more than high school but not college": POE3,
           "college": POE4}
    return POE
    raise NotImplementedError

def average_influenza_doses():
    import pandas as pd
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 10)
    import numpy as np
    df = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\NISPUF17.csv", index_col=0)
    df = df.loc[:, ["CBF_01", "P_NUMFLU"]].dropna() #filter out missing values in P_NUMFLU
    print(df)
    n_bf = len(df[df["CBF_01"] == 1])
    n_nbf = len(df[df["CBF_01"] == 2])
    P1 = df[df["CBF_01"] == 1]["P_NUMFLU"].sum() / n_bf  # specify only wants to focus on
    P2 = df[df["CBF_01"] == 2]["P_NUMFLU"].sum() / n_nbf  # specify only wants to focus on
    return(P1, P2)
print(average_influenza_doses())











