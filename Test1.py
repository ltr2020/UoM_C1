import pandas as pd
import numpy as np

# Question 1
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
    print(Energy)
    Energy["Energy Supply"] = Energy["Energy Supply"]*10**6
    Energy["Country"] = Energy["Country"].replace(to_replace=r"\d*", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace(to_replace=r"\s\(.*\)", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace({"Republic of Korea": "South Korea",
                                                       "United States of America": "United States",
                                                       "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                                       "China, Hong Kong Special Administrative Region": "Hong Kong"})

    print("Bolivia" in Energy["Country"].values)   #important to add in .values to check if a column contain certain value
    print("Switzerland" in Energy["Country"].values)
    print("United States" in Energy["Country"].values)

    GDP = pd.read_csv(r"Doc\world_bank.csv", skiprows=4)
    print(GDP.head())
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.": "South Korea",
                                                       "Iran, Islamic Rep.": "Iran",
                                                       "Hong Kong SAR, China": "Hong Kong"})
    print("Hong Kong" in GDP["Country Name"].values)

    ScimEn = pd.read_excel(r"Doc/scimagojr-3.xlsx")
    print(ScimEn.head())

    GDP06_15 = GDP[["Country Name","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]]
    GDP06_15 = GDP06_15.rename(columns={"Country Name": "Country"})

    print(GDP06_15.head())
    merge1 = pd.merge(Energy, GDP06_15, how="inner",
                      left_on="Country", right_on="Country").set_index("Country")
    print(merge1.head())
    ScimEn_top15 = ScimEn[ScimEn["Rank"]<=15]
    del ScimEn_top15["Region"]
    merge2 = pd.merge(ScimEn_top15, merge1, how="inner",
                      left_on="Country", right_on="Country").set_index("Country")
    return merge2
assert type(answer_one()) == pd.DataFrame, "Q1: You should return a DataFrame!"

assert answer_one().shape == (15,20), "Q1: Your DataFrame should have 20 columns and 15 entries!"


