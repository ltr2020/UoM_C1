import pandas as pd

price = pd.Series([1000,2000,3000]) #default index 0,1,2
price = pd.Series([1000,2000,3000], index=["S10","S11","S12"]) #change index
print(price)
price_dict = {"S10": 1000, "S11": 2000, "S12": 3000}
price = pd.Series(price_dict) #convert dict to Series
print(price)
print("")
price["S10"] = 1500
print(price.index)
print(price.values)


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
 'year': [2000, 2001, 2002, 2001, 2002, 2003],
 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
