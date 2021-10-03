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
merge1 = pd.merge(staff_df, student_df, how="outer", on="Name")  #use index both df have as index
print(merge1)
merge2 = pd.merge(staff_df, student_df, how="inner", left_index=True, right_index=True)
print(merge2)
merge3 = pd.merge(staff_df, student_df, how="left", left_index=True, right_index=True)
print(merge3)
merge4 = pd.merge(staff_df, student_df, how="right", left_index=True, right_index=True)
print(merge4)
print(len(merge4))
print("")

print("OneA Merging datasets")
print("pd.concat([df1, df2, df3]")
print("")

print("TwoA - Chaining")
df = pd.read_csv('Doc\census.csv')
df1 = (df.where(df['SUMLEV']==50)
      .dropna()
      .set_index(['STNAME', 'CTYNAME'])
      .rename(columns={"ESTIMATESBASE2010":'EstBase2010'}))
print(df1.head())
print("or, much faster but less readability")
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
    row["MIN"] = np.min(data)
    return row
df_min_max = df.apply(min_max, axis="columns").head()
print("")

row = ["POPESTIMATE2010",
       "POPESTIMATE2011",
       "POPESTIMATE2012",
       "POPESTIMATE2013",
       "POPESTIMATE2014",
       "POPESTIMATE2015"]
df_min_max2 = df.apply(lambda x: [np.max(x[row]), np.min(x[row])], axis="columns").head()
print("")

print(df["STNAME"].tolist())
def Country(x):
    USA = df["STNAME"].tolist()
    if x in USA:
        return "USA"
df["Country"] = df["STNAME"].apply(lambda x: Country(x))    #create new column
print(df[["STNAME","Country"]])
del df["Country"]
print("")

print("TwoC - groupby() to split df into chunks to speed up")
def method_slow():
    for state in df["STNAME"].unique():
        avg = np.average(df[df["STNAME"]==state].dropna()["CENSUS2010POP"])
        return("Counties in state " + state + " have an avg pop of " + str(avg))

def method_fast():
    for group, frame in df.groupby("STNAME"):   ##pass a column to groupby(), o/w default index
        avg = np.average(frame["CENSUS2010POP"])
        return("Counties in state " + state + " have an avg pop of " + str(avg))
print("")

df= pd.read_csv("Doc/listings.csv")
print(df)


