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

print(proportion_of_education())


