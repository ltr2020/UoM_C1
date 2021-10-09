import pandas as pd
import numpy as np

print("Question 1")
# Load assets/Energy Indicators.xls and put into a DataFrame with the variable name of Energy
# make sure to exclude the footer and header information from the datafile
# first two columns are unneccessary, get rid of them
# change the column labels so that the columns are:
# ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]
# Convert Energy Supply to gigajoules (Note: 1,000,000 gigajoules = petajoule）
# all countries missing data (e.g. data with "...") make sure reflected as np.NaN values
# Rename the following list of countries:
# "Republic of Korea": "South Korea",
#"United States of America": "United States",
#"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
#"China, Hong Kong Special Administrative Region": "Hong Kong"
# several countries with numbers and/or parenthesis in their name. Be sure to remove these,
# e.g. 'Bolivia (Plurinational State of)' should be 'Bolivia'. 'Switzerland17' should be 'Switzerland'

# load the GDP data from the file assets/world_bank.csv, which is a csv containing countries'. Call this DataFrame GDP
# skip the header, and rename the following list of countries:
#"Korea, Rep.": "South Korea",
#"Iran, Islamic Rep.": "Iran",
#"Hong Kong SAR, China": "Hong Kong"

# load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file assets/scimagojr-3.xlsx
# which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn

# Join the three datasets: GDP, Energy, and ScimEn into a new dataset using the intersection of country names)
# Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15)
# index = name of country
# columns = columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

import pandas as pd
import numpy as np
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

def answer_one():
    Energy = pd.read_excel(r"Doc/Energy Indicators.xls",
                           skiprows=18, skipfooter= 283-246,
                           usecols=[2,3,4,5],
                           names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
                           header=None,
                           na_values=["..."]
                           )

    Energy["Energy Supply"] = Energy["Energy Supply"]*10**6
    Energy["Country"] = Energy["Country"].replace(to_replace=r"\d*", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace(to_replace=r"\s\(.*\)", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace({"Republic of Korea": "South Korea",
                                                       "United States of America": "United States",
                                                       "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                                       "China, Hong Kong Special Administrative Region": "Hong Kong"})

    "Bolivia" in Energy["Country"].values   #important to add in .values to check if a column contain certain value

    GDP = pd.read_csv(r"Doc\world_bank.csv", skiprows=4)
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.": "South Korea",
                                                       "Iran, Islamic Rep.": "Iran",
                                                       "Hong Kong SAR, China": "Hong Kong"})
    "Hong Kong" in GDP["Country Name"].values

    ScimEn = pd.read_excel(r"Doc/scimagojr-3.xlsx")

    GDP06_15 = GDP[["Country Name","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]]
    GDP06_15 = GDP06_15.rename(columns={"Country Name": "Country"})

    merge1 = pd.merge(Energy, GDP06_15, how="inner",
                      left_on="Country", right_on="Country").set_index("Country")

    ScimEn_top15 = ScimEn[ScimEn["Rank"]<=15]
    del ScimEn_top15["Region"]
    merge2 = pd.merge(ScimEn_top15, merge1, how="inner",
                      left_on="Country", right_on="Country").set_index("Country")
    return merge2
print(answer_one())
#check
assert type(answer_one()) == pd.DataFrame, "Q1: You should return a DataFrame!"
assert answer_one().shape == (15,20), "Q1: Your DataFrame should have 20 columns and 15 entries!"
print("")

print("Question 2")
#When you joined the datasets, but before you reduced this to the top 15 items,
# how many entries did you lose?
def answer_two():
    Energy = pd.read_excel("Doc/Energy Indicators.xls",
                           skiprows=18, skipfooter=283 - 246,
                           usecols=[2, 3, 4, 5],
                           names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
                           header=None,
                           na_values=["..."]
                           )
    Energy["Energy Supply"] = Energy["Energy Supply"] * 10 ** 6
    Energy["Country"] = Energy["Country"].replace(to_replace=r"\d*", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace(to_replace=r"\s\(.*\)", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace({"Republic of Korea": "South Korea",
                                                   "United States of America": "United States",
                                                   "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                                   "China, Hong Kong Special Administrative Region": "Hong Kong"})

    GDP = pd.read_csv("Doc/world_bank.csv", skiprows=4)
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.": "South Korea",
                                                       "Iran, Islamic Rep.": "Iran",
                                                       "Hong Kong SAR, China": "Hong Kong"})

    ScimEn = pd.read_excel("Doc/scimagojr-3.xlsx")

    GDP06_15 = GDP[["Country Name", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]]
    GDP06_15 = GDP06_15.rename(columns={"Country Name": "Country"})
    inner1 = pd.merge(Energy, GDP06_15, how="inner",
                      left_on="Country", right_on="Country").set_index("Country")

    inner2 = pd.merge(ScimEn, inner1, how="inner",
                      left_on="Country", right_on="Country").set_index("Country")

    outer = pd.concat([GDP06_15, ScimEn, Energy])["Country"].unique()

    return len(outer) - len(inner2)
    raise NotImplementedError()
print(answer_two())
print("")

print("Question 3")
# What are the top 15 countries for average GDP over the last 10 years?

# return a Series named avgGDP with 15 countries
# and their average GDP sorted in descending order

def answer_three():
    top15 = answer_one()
    top15 = top15.iloc[:,10:]
    avgGDP = top15.apply(np.nanmean, axis=1).sort_values(ascending=False)
    #or use agg instead of apply
    # apply() applies func to each grp
    # agg() applies each column for each grp, also can >1 func
    return avgGDP
print(answer_three())

print("Question 4")
# By how much had the GDP changed over the 10 year span
# for the country with the 6th largest average GDP?
# This function should return a single number

def answer_four():
    top15 = answer_one()
    avgGDP = answer_three()
    #France is the 6th country
    top15["avgGDP"] = avgGDP
    top15_sortGDP = top15.sort_values(["avgGDP"], ascending=False)
    change = top15_sortGDP.iloc[5]["2015"] - top15_sortGDP.iloc[5]["2006"]
    return change
    raise NotImplementedError()
print(answer_four())
print("")

print("Question 5")
# What is the mean energy supply per capita?
# This function should return a single number.
def answer_five():
    top15 = answer_one()
    mean_En = top15["Energy Supply per Capita"].mean()
    return mean_En
print(answer_five())
print("")

print("Question 6")
# What country has the maximum % Renewable and what is the percentage?
# This function should return a tuple with the name of the country and the percentage.
def answer_six():
    top15 = answer_one()
    top15_sortRe = top15["% Renewable"].sort_values(ascending=False)
    return(top15_sortRe.index[0], top15_sortRe.max())
print(answer_six())
assert type(answer_six()) == tuple, "Q6: You should return a tuple!"
assert type(answer_six()[0]) == str, "Q6: The first element in your result should be the name of the country!"
print("")

print("Question 7")
# Create a new column that is the ratio of Self-Citations to Total Citations
# What is the maximum value for this new column, and what country has the highest ratio?
# This function should return a tuple with the name of the country and the ratio.
def answer_seven():
    top15 = answer_one()
    top15["% Self Citations"] = top15["Self-citations"]/top15["Citations"]
    top15_selfcite = top15["% Self Citations"].sort_values(ascending=False)
    return (top15_selfcite.index[0], top15_selfcite.max())
print(answer_seven())
assert type(answer_seven()) == tuple, "Q7: You should return a tuple!"
assert type(answer_seven()[0]) == str, "Q7: The first element in your result should be the name of the country!"
print("")

def answer_eight():
    top15 = answer_one()
    top15["Est_Pop"] = top15["Energy Supply"] / top15["Energy Supply per Capita"]
    top15_sortPop = top15["Est_Pop"].sort_values(ascending=False)
    third_Pop = top15_sortPop.index[2]
    return third_Pop
print(answer_eight())
print("")

print("Question 9")
# Create a column that estimates the number of citable documents per person.
# What is the correlation between the number of citable documents per capita and the energy supply per capita?
# Use the .corr() method, (Pearson's correlation).
# This function should return a single number.
# (Optional: Use the built-in function plot9() to visualize the relationship
# between Energy Supply per Capita vs. Citable docs per Capita)
top15 = answer_one()
top15["Est_Pop"] = top15["Energy Supply"] / top15["Energy Supply per Capita"]
top15["CiteDoc_per_capita"] = top15["Citable documents"] / top15["Est_Pop"]
print(top15["CiteDoc_per_capita"].corr(top15["Energy Supply per Capita"]))
