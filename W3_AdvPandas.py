import pandas as pd
import numpy as np
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
staff_df = pd.DataFrame({"Name":["Kelly", "Sally", "James"],
                         "Role":["Director of HR", "Course liasion", "Grader"],
                         "Location":["x", "y", "z"]})
student_df = pd.DataFrame({"Name":["James", "Mike", "Sally"],
                         "School":["Business", "Law", "Engineering"],
                           "Location":["a", "b", "c"]})
print("One Merging dataframes")
staff_df = staff_df.set_index("Name")
student_df = student_df.set_index("Name")
print(staff_df)
print(student_df)
merge = pd.merge(staff_df, student_df, how="outer", on="Name")  #use index both df have as index
print(merge)
merge = pd.merge(staff_df, student_df, how="inner", left_index=True, right_index=True)
print(merge)
merge = pd.merge(staff_df, student_df, how="left", left_index=True, right_index=True)
print(merge)
merge = pd.merge(staff_df, student_df, how="right", left_index=True, right_index=True)
print(merge)
print(len(merge))
print("")

print("OneA Merging datasets")
print("pd.concat([df1, df2, df3]")
print("")

print("TwoA - Chaining")
df = pd.read_csv(r'C:\Users\user\PycharmProjects\UoM_C1\Doc\census.csv')
df1 = (df.where(df['SUMLEV']==50)
      .dropna()
      .set_index(['STNAME', 'CTYNAME'])
      .rename(columns={"ESTIMATESBASE2010":'EstBase2010'}))
print(df1.head())
print("or, much faster but lessmreadability")
df2 = (df[df["SUMLEV"]==50]
       .set_index(['STNAME', 'CTYNAME'])
       .rename(columns={"ESTIMATESBASE2010":'EstBase2010'}))
print(df2.head())
print("")

print("TwoB - .aaply & lambda to add new columns")
def min_max(row):
    data = row[["POPESTIMATE2010",
               "POPESTIMATE2011",
               "POPESTIMATE2012",
               "POPESTIMATE2013",
               "POPESTIMATE2014",
               "POPESTIMATE2015"
               ]]
    row["MAX"] = np.max(data)
    row ["MIN"] = np.min(data)
    return row
print(df.apply(min_max, axis="columns").head())
print("")

row = ["POPESTIMATE2010",
       "POPESTIMATE2011",
       "POPESTIMATE2012",
       "POPESTIMATE2013",
       "POPESTIMATE2014",
       "POPESTIMATE2015"]
print(df.apply(lambda x: [np.max(x[row]), np.min(x[row])], axis="columns").head())
print("")

print(df["STNAME"].tolist())
def Country(x):
    USA = df["STNAME"].tolist()
    if x in USA:
        return "USA"
df["Country"] = df["STNAME"].apply(lambda x: country(x))
print(df[["STNAME","Country"]])

