import re
import numpy as np
import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


print("One")
price = pd.Series([1000,2000,3000]) #default index 0,1,2
price = pd.Series([1000,2000,3000], index=["S10","S11","S12"]) #change index
price.name = "price"
price.index.name = "MODEL"
print(price)
print("")
#or use dict
price_dict = {"S10": 1000, "S11": 2000, "S12": 3000}
model = ["S10", "S11", "S12", "S20"]    #no data for S20 column --> NaN
price = pd.Series(price_dict, index=model) #convert dict to Series
print(price)
print("")

print("OneA")
price["S10"] = 1500 #mutable like list e.g. append, alter value
print(price.index)
print(price.values)
print(price[2]) #attribute so use index operator, retrieve value by index
print(price.loc["S20"]) #or retrieve value by key
print(price[price>1800]) #filter
print("S12" in price)
print("")


print("OneB")
print(price.isnull()) #to check if there's any missing value
print("")

#for loop but it's not simultaneous
grades = pd.Series([90, 80, 70, 60])
total = 0
for grade in grades:
 total += grade
avg = total/len(grades)

#vectorisaton using numpy much faster on big Series, esp with good grahpics
total1 = np.sum(grades)
avg1 = total1/len(grades)

#DataFrame
print("Two")
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, columns=["year", "state", "pop", "debt"]) #arrange column
value = pd.Series ([-1.5, -2, -3], index = [0, 3, 4]) #assign list, array, series to DataFrame
frame["debt"] = value
print(frame)

print("TwoA")
frame['eastern'] = frame.state == 'Ohio' #create a new column
print(frame)
print(frame.loc[:, ["year", "state", "pop", "debt"]])
del frame["eastern"]
print("")

print(frame.loc[3]) #retrieve row by index
print(frame["state"])   #retrieve column
print("")

#or seperately but slower
record1 = pd.Series({"state": "Ohio",
                     "year": 2000,
                     "pop": 1.5})
record2 = pd.Series({"state": "Ohio",
                     "year": 2001,
                     "pop": 1.7})
record3 = pd.Series({"state": "Ohio",
                     "year": 2002,
                     "pop": 3.6})
frame1 = pd.DataFrame([record1, record2, record3])
print(frame.T)  #transpose
print("")

#Drop function or use del
print(frame.drop("state", inplace=False, axis=1))    #drop row and column, inplace=True (don't create new object alter original), axis=0 by default
#or
del frame["state"]  #and print this
print("")

print("TwoB")
df = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\Admission_Predict.csv", index_col=1)
print(df.head())    #default 5
print("")

#using dict to change column name
df = df.rename(mapper=str.strip, axis="columns")    #str.strip() to strip space

df_new = df.rename(columns={"LOR":"Letter of Recom",
                            "SOP":"Statement of Purpose"})
print(df_new.columns)

#filter and missing values (boolean mask)
criteria = df[df["Chance of Admit"]>0.7]    #include .where() & .dropna
print(criteria)
#and
criteria = df["Chance of Admit"].gt(0.7).lt(0.9)    #0.7<x<0.9
print(df.where(criteria).dropna().head())   #.dropna() removes entries outside 0.7< x <0.9


criteria.fillna(0, inplace=True)    #fill missing value with "0"

print("")

#set a column to be new index
df.index = df["Research"]
# or df = df.set_index(["Research"]); can use double columns as index
print(df["Research"].unique()) #unique value in research
df.filter = df[df["Research"] == 1]
print(df.filter.head())
#df.loc[(index1_1, index1_2,...), (index2_1, index2_2,...)]

#Missing Value
print("TwoC")
CG = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\class_grades.csv")
# for large file, without any missing value, add na_filter=False can improve perf
CG_drop = CG.dropna()    #drop missing values
CG.fillna(0, inplace=True)
#modify original dataframe all missing values to 0
print(CG.head())
print("")

#Another example
LOG = pd.read_csv(r"C:\Users\user\PycharmProjects\UoM_C1\Doc\log.csv")  #no chan個--》missing values
print(LOG.head(10))
LOG = LOG.set_index(["time", "user"]) #multi-level indexing
LOG = LOG.sort_index()  #sort by index
LOG = LOG.fillna(method = "ffill")  #to fill missing values with previous row entry
#bfill vice versa

print(LOG.head())