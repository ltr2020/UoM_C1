#Series
price = pd.Series([1000,2000,3000]) #default index 0,1,2
price = pd.Series([1000,2000,3000], index=["S10","S11","S12"]) #change index
price.name = "price"
price.index.name = "MODEL"
print(price)
print("")

price_dict = {"S10": 1000, "S11": 2000, "S12": 3000}
model = ["S10", "S11", "S12", "S20"]
price = pd.Series(price_dict, index=model) #convert dict to Series
print(price)
print("")

price["S10"] = 1500 #mutable like list
print(price.index)
print(price.values)
print(price[price>1800]) #filter
print("S20" in price)
print(pd.isnull(price))
print("")

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

print(frame.loc[3]) #retrieve row
print(frame["state"])
