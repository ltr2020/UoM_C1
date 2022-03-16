# Question 1
# Write a function called proportion_of_education
# which returns the proportion of children in the dataset
# who had a mother with the education levels equal to less than high
# school (<12), high school (12), more than high school but not a college
# graduate (>12) and college degree.

# This function should return a dictionary in the form of (use the correct
# numbers, do not round numbers):

def proportion_of_education():
    import pandas as pd
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 10)
    import numpy as np
    df = pd.read_csv(r"Doc/NISPUF17.csv", index_col=0)
    n = len(df["EDUC1"])
    POE1 = len(df[df["EDUC1"] == 1]) / n
    # or
    POE2 = (np.sum(df["EDUC1"] == 2)) / n
    POE3 = (np.sum(df["EDUC1"] == 3)) / n
    POE4 = (np.sum(df["EDUC1"] == 4)) / n
    POE = {"less than high school": POE1,
           "high school": POE2,
           "more than high school but not college": POE3,
           "college": POE4}
    return POE
    raise NotImplementedError()


print(proportion_of_education())

assert isinstance(proportion_of_education(), type({})
                  ), "You must return a dictionary."
assert len(proportion_of_education()
           ) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(
), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(
), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education(
).keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(
), "You have not returned a dictionary with the correct keys."

# Question 2
# Let’s explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine
# from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.
# This function should return a tuple in the form (use the correct numbers:


def average_influenza_doses():
    import pandas as pd
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 10)
    import numpy as np
    df = pd.read_csv(r"Doc/NISPUF17.csv", index_col=0)
    df = df.loc[:, ["CBF_01", "P_NUMFLU"]]
    df = df[df["P_NUMFLU"].notna()]  # filter out missing values in P_NUMFLU
    n_bf = len(df[df["CBF_01"] == 1])
    n_nbf = len(df[df["CBF_01"] == 2])
    # specify only wants to focus on
    P1 = df[df["CBF_01"] == 1]["P_NUMFLU"].sum() / n_bf
    # specify only wants to focus on
    P2 = df[df["CBF_01"] == 2]["P_NUMFLU"].sum() / n_nbf
    return(P1, P2)
    raise NotImplementedError()


print(average_influenza_doses())
assert len(average_influenza_doses(
)) == 2, "Return two values in a tuple, the first for yes and the second for no."

# Question 3
# It would be interesting to see if there is any evidence of a link between vaccine effectiveness
# and sex of the child. Calculate the ratio of the number of children who contracted chickenpox
# but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.
# This function should return a dictionary in the form of (use the correct
# numbers)


def chickenpox_by_sex():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    df = pd.read_csv(r"Doc\NISPUF17.csv", index_col=0)
    df = df.loc[:, ["HAD_CPOX", "P_NUMVRC", "SEX"]].dropna()
    criteria1 = (
        df["SEX"] == 1) & (
        df["HAD_CPOX"] == 1) & (
            df["P_NUMVRC"] >= 1)
    criteria2 = (
        df["SEX"] == 1) & (
        df["HAD_CPOX"] == 2) & (
            df["P_NUMVRC"] >= 1)
    criteria3 = (
        df["SEX"] == 2) & (
        df["HAD_CPOX"] == 1) & (
            df["P_NUMVRC"] >= 1)
    criteria4 = (
        df["SEX"] == 2) & (
        df["HAD_CPOX"] == 2) & (
            df["P_NUMVRC"] >= 1)
    cpox1_vrc1_sex1 = len(df.where(criteria1).dropna())
    cpox2_vrc1_sex1 = len(df.where(criteria2).dropna())
    cpox1_vrc1_sex2 = len(df.where(criteria3).dropna())
    cpox2_vrc1_sex2 = len(df.where(criteria4).dropna())
    ratio = {"male": cpox1_vrc1_sex1 / cpox2_vrc1_sex1,
             "female": cpox1_vrc1_sex2 / cpox2_vrc1_sex2}
    return ratio
    raise NotImplementedError()


print(chickenpox_by_sex())
assert len(chickenpox_by_sex(
)) == 2, "Return a dictionary with two items, the first for males and the second for females."

# Question 4
# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).
# Some notes on interpreting the answer. The had_chickenpox_column is either 1 (for yes) or 2 (for no), and the num_chickenpox_vaccine_column is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., corr > 0) means that an increase in had_chickenpox_column (which means more no’s) would also increase the values of num_chickenpox_vaccine_column (which means more doses of vaccine). If there is a negative correlation (e.g., corr < 0), it indicates that having had chickenpox is related to an increase in the number of vaccine doses.
# Also, pval is the probability that we observe a correlation between had_chickenpox_column and num_chickenpox_vaccine_column which is greater than or equal to a particular value occurred by chance. A small pval means that the observed correlation is highly unlikely to occur by chance. In this case, pval should be very small (will end in e-18 indicating a very small number).
# [1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose?


def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    df = pd.read_csv(r"Doc\NISPUF17.csv", index_col=0)
    df = df[["HAD_CPOX", "P_NUMVRC"]].dropna()
    df = df[df["HAD_CPOX"] <= 2].dropna()
    corr, pval = stats.pearsonr(df["HAD_CPOX"], df["P_NUMVRC"])
    return corr
    raise NotImplementedError()


print(corr_chickenpox())
assert -1 <= corr_chickenpox() <= 1, "You must return a float number between -1.0 and 1.0."
