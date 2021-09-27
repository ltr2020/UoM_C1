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
print(proportion_of_education())

assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."


def average_influenza_doses():
    # YOUR CODE HERE
    import pandas as pd
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 10)
    import numpy as np
    df = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\NISPUF17.csv", index_col=0)
    df = df.loc[:, ["CBF_01", "P_NUMFLU"]]
    df = df[df["P_NUMFLU"].notna()] #filter out missing values in P_NUMFLU
    n_bf = len(df[df["CBF_01"] == 1])
    n_nbf = len(df[df["CBF_01"] == 2])
    P1 = df[df["CBF_01"] == 1]["P_NUMFLU"].sum() / n_bf  # specify only wants to focus on
    P2 = df[df["CBF_01"] == 2]["P_NUMFLU"].sum() / n_nbf  # specify only wants to focus on
    return(P1, P2)
    raise NotImplementedError()
print(average_influenza_doses())
assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."

def chickenpox_by_sex():
    import pandas as pd
    df = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\NISPUF17.csv", index_col=0)
    df = df.loc[:,["HAD_CPOX", "P_NUMVRC", "SEX"]].dropna()
    criteria1= (df["SEX"]==1) & (df["HAD_CPOX"]==1) & (df["P_NUMVRC"]>=1)
    criteria2= (df["SEX"]==1) & (df["HAD_CPOX"]==2) & (df["P_NUMVRC"]>=1)
    criteria3= (df["SEX"]==2) & (df["HAD_CPOX"]==1) & (df["P_NUMVRC"]>=1)
    criteria4= (df["SEX"]==2) & (df["HAD_CPOX"]==2) & (df["P_NUMVRC"]>=1)
    cpox1_vrc1_sex1 = len(df.where(criteria1).dropna())
    cpox2_vrc1_sex1 = len(df.where(criteria2).dropna())
    cpox1_vrc1_sex2 = len(df.where(criteria3).dropna())
    cpox2_vrc1_sex2 = len(df.where(criteria4).dropna())
    ratio = {"male": cpox1_vrc1_sex1 / cpox2_vrc1_sex2,
        "female": cpox1_vrc1_sex2 / cpox2_vrc1_sex2}
    return ratio
    raise NotImplementedError()
print(chickenpox_by_sex())
assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    df = pd.read_csv(r"assets/NISPUF17.csv", index_col=0)
    df = df[["HAD_CPOX","P_NUMVRC"]].dropna()
    df = df[df["HAD_CPOX"]<=2].dropna()
    corr, pval = stats.pearsonr(df["HAD_CPOX"],df["P_NUMVRC"])
    return corr
    raise NotImplementedError()
assert -1<=corr_chickenpox()<=1, "You must return a float number between -1.0 and 1.0."






