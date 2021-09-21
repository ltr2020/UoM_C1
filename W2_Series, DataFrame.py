import pandas as pd
import numpy as np

#Series
price = pd.Series([1000,2000,3000]) #default index 0,1,2
price = pd.Series([1000,2000,3000], index=["S10","S11","S12"]) #change index
price.name = "price"
price.index.name = "MODEL"
print(price)
print("")
#or
price_dict = {"S10": 1000, "S11": 2000, "S12": 3000}
model = ["S10", "S11", "S12", "S20"]
price = pd.Series(price_dict, index=model) #convert dict to Series
print(price)
print("")

price["S10"] = 1500 #mutable like list e.g. append, alter value
print(price.index)
print(price.values)
print(price[3]) #attribute so use index operator, retrieve value by index
print(price.loc["S20"]) #retrieve value by key
print(price[price>1800]) #filter
print("S20" in price)
print(pd.isnull(price))
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
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
 'year': [2000, 2001, 2002, 2001, 2002, 2003],
 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, columns=["year", "state", "pop", "debt"]) #arrange column
value = pd.Series ([-1.5, -2, -3], index = [0, 3, 4]) #assign list, array, series to DataFrame
frame["debt"] = value
frame['eastern'] = frame.state == 'Ohio' #create a new column
print(frame)
del frame["eastern"]
print("")

record1 = pd.Series(["Ohio"[3], "Nevada"[3]])
record2 = pd.Series([range(2000,2004)])
record3 = pd.Series([1.5, 1.7, 3.6, 2.4, 2.9, 3.2])
frame = pd.DataFrame([record1, record2, record3])
print(frame)

print(frame.loc[3]) #retrieve row
print(frame["state"])
print("")

