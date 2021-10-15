import numpy as np
import pandas as pd

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
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"
# several countries with numbers and/or parenthesis in their name. Be sure to remove these,
# e.g. 'Bolivia (Plurinational State of)' should be 'Bolivia'.
# 'Switzerland17' should be 'Switzerland'

# load the GDP data from the file assets/world_bank.csv, which is a csv containing countries'. Call this DataFrame GDP
# skip the header, and rename the following list of countries:
# "Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"

# load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file assets/scimagojr-3.xlsx
# which ranks countries based on their journal contributions in the
# aforementioned area. Call this DataFrame ScimEn

# Join the three datasets: GDP, Energy, and ScimEn into a new dataset using the intersection of country names)
# Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15)
# index = name of country
# columns = columns should be ['Rank', 'Documents', 'Citable documents',
# 'Citations', 'Self-citations', 'Citations per document', 'H index',
# 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006',
# '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)


def answer_one():
    Energy = pd.read_excel(
        r"Doc/Energy Indicators.xls",
        skiprows=18,
        skipfooter=283 - 246,
        usecols=[
            2,
            3,
            4,
            5],
        names=[
            'Country',
            'Energy Supply',
            'Energy Supply per Capita',
            '% Renewable'],
        header=None,
        na_values=["..."])

    Energy["Energy Supply"] = Energy["Energy Supply"] * 10 ** 6
    Energy["Country"] = Energy["Country"].replace(
        to_replace=r"\d*", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace(
        to_replace=r"\s\(.*\)", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace(
        {
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"})

    # important to add in .values to check if a column contain certain value
    "Bolivia" in Energy["Country"].values

    GDP = pd.read_csv(r"Doc\world_bank.csv", skiprows=4)
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.": "South Korea",
                                                       "Iran, Islamic Rep.": "Iran",
                                                       "Hong Kong SAR, China": "Hong Kong"})
    "Hong Kong" in GDP["Country Name"].values

    ScimEn = pd.read_excel(r"Doc/scimagojr-3.xlsx")

    GDP06_15 = GDP[["Country Name", "2006", "2007", "2008",
                    "2009", "2010", "2011", "2012", "2013", "2014", "2015"]]
    GDP06_15 = GDP06_15.rename(columns={"Country Name": "Country"})

    merge1 = pd.merge(
        Energy,
        GDP06_15,
        how="inner",
        left_on="Country",
        right_on="Country").set_index("Country")

    ScimEn_top15 = ScimEn[ScimEn["Rank"] <= 15]
    del ScimEn_top15["Region"]
    merge2 = pd.merge(
        ScimEn_top15,
        merge1,
        how="inner",
        left_on="Country",
        right_on="Country").set_index("Country")
    return merge2


print(answer_one())
# check
assert isinstance(
    answer_one(), pd.DataFrame), "Q1: You should return a DataFrame!"
assert answer_one().shape == (
    15, 20), "Q1: Your DataFrame should have 20 columns and 15 entries!"
print("")

print("Question 2")


# When you joined the datasets, but before you reduced this to the top 15 items,
# how many entries did you lose?


def answer_two():
    Energy = pd.read_excel(
        "Doc/Energy Indicators.xls",
        skiprows=18,
        skipfooter=283 - 246,
        usecols=[
            2,
            3,
            4,
            5],
        names=[
            'Country',
            'Energy Supply',
            'Energy Supply per Capita',
            '% Renewable'],
        header=None,
        na_values=["..."])
    Energy["Energy Supply"] = Energy["Energy Supply"] * 10 ** 6
    Energy["Country"] = Energy["Country"].replace(
        to_replace=r"\d*", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace(
        to_replace=r"\s\(.*\)", value="", regex=True)
    Energy["Country"] = Energy["Country"].replace(
        {
            "Republic of Korea": "South Korea",
            "United States of America": "United States",
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "China, Hong Kong Special Administrative Region": "Hong Kong"})

    GDP = pd.read_csv("Doc/world_bank.csv", skiprows=4)
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.": "South Korea",
                                                       "Iran, Islamic Rep.": "Iran",
                                                       "Hong Kong SAR, China": "Hong Kong"})

    ScimEn = pd.read_excel("Doc/scimagojr-3.xlsx")

    GDP06_15 = GDP[["Country Name", "2006", "2007", "2008",
                    "2009", "2010", "2011", "2012", "2013", "2014", "2015"]]
    GDP06_15 = GDP06_15.rename(columns={"Country Name": "Country"})
    inner1 = pd.merge(
        Energy,
        GDP06_15,
        how="inner",
        left_on="Country",
        right_on="Country").set_index("Country")

    inner2 = pd.merge(
        ScimEn,
        inner1,
        how="inner",
        left_on="Country",
        right_on="Country").set_index("Country")

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
    top15 = top15.iloc[:, 10:]
    avgGDP = top15.apply(np.nanmean, axis=1).sort_values(ascending=False)
    # or use agg instead of apply
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
    # France is the 6th country
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
# This function should return a tuple with the name of the country and the
# percentage.


def answer_six():
    top15 = answer_one()
    top15_sortRe = top15["% Renewable"].sort_values(ascending=False)
    return (top15_sortRe.index[0], top15_sortRe.max())


print(answer_six())
assert isinstance(answer_six(), tuple), "Q6: You should return a tuple!"
assert isinstance(answer_six()[
    0], str), "Q6: The first element in your result should be the name of the country!"
print("")

print("Question 7")


# Create a new column that is the ratio of Self-Citations to Total Citations
# What is the maximum value for this new column, and what country has the highest ratio?
# This function should return a tuple with the name of the country and the
# ratio.


def answer_seven():
    top15 = answer_one()
    top15["% Self Citations"] = top15["Self-citations"] / top15["Citations"]
    top15_selfcite = top15["% Self Citations"].sort_values(ascending=False)
    return (top15_selfcite.index[0], top15_selfcite.max())


print(answer_seven())
assert isinstance(answer_seven(), tuple), "Q7: You should return a tuple!"
assert isinstance(answer_seven()[
    0], str), "Q7: The first element in your result should be the name of the country!"
print("")


def answer_eight():
    top15 = answer_one()
    top15["Est_Pop"] = top15["Energy Supply"] / \
        top15["Energy Supply per Capita"]
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


def answer_nine():
    top15 = answer_one()
    top15["Est_Pop"] = top15["Energy Supply"] / \
        top15["Energy Supply per Capita"]
    top15["CiteDoc_per_capita"] = top15["Citable documents"] / top15["Est_Pop"]
    return (top15["CiteDoc_per_capita"].corr(
        top15["Energy Supply per Capita"]))
    raise NotImplementedError()


print(answer_nine())
assert answer_nine() >= - \
    1. and answer_nine() <= 1., "Q9: A valid correlation should between -1 to 1!"


def plot9():
    import matplotlib.pyplot as plt
    # %matplotlib inline in ipynb
    Top15 = answer_one()
    Top15['Est_Pop'] = Top15['Energy Supply'] / \
        Top15['Energy Supply per Capita']
    Top15['CiteDoc_per_capita'] = Top15['Citable documents'] / Top15['Est_Pop']
    Top15.plot(
        x='CiteDoc_per_capita',
        y='Energy Supply per Capita',
        kind='scatter',
        xlim=[
            0,
            0.0006])
    return plt.show()


print("")

print("Question 10")


# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15,
# and a 0 if the country's % Renewable value is below the median.
# This function should return a series named
# HighRenew whose index is the country name sorted in ascending order of rank.


def answer_ten():
    top15 = answer_one()
    median_Re = top15["% Renewable"].median()
    top15["HighRenew"] = top15["% Renewable"].apply(
        lambda x: 0 if x < median_Re else 1)
    # or top15["HighRenew"] = [0 if x < median_Re else 1 for x in top15["%
    # Renewable"]]
    return (top15["HighRenew"])
    raise NotImplementedError()


print(answer_ten())
assert isinstance(answer_ten(), pd.Series), "Q10: You should return a Series!"
print("")

print("Question 11")


# Use the following dictionary to group the Countries by Continent
# then create a DataFrame that displays the sample size (the number of countries in each continent bin)
# and the sum, mean, and std deviation for the estimated population of
# each country


def answer_eleven():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    top15 = answer_one()
    top15["Est_Pop"] = top15["Energy Supply"] / \
        top15["Energy Supply per Capita"]
    top15["Continent"] = pd.Series(ContinentDict)
    return top15.groupby("Continent")["Est_Pop"].agg(
        Size=np.size, Sum=np.sum, Mean=np.mean, Std_dev=np.std)

    # can't use dict inside of agg() old method


print(answer_eleven())
assert isinstance(
    answer_eleven(), pd.DataFrame), "Q11: You should return a DataFrame!"
assert answer_eleven().shape[0] == 5, "Q11: Wrong row numbers!"
assert answer_eleven().shape[1] == 4, "Q11: Wrong column numbers!"
print("")

print("Question 12")


# Cut % Renewable into 5 bins
# Group Top15 by the Continent, as well as these new % Renewable bins.
# How many countries are in each of these groups?
# This function should return a Series with a MultiIndex of Continent,
# then the bins for % Renewable. Do not include groups with no countries.


def answer_twelve():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    top15 = answer_one()
    top15["Continent"] = pd.Series(ContinentDict)
    top15["% Renewable"] = pd.cut(top15["% Renewable"], 5)
    top15["% Renewable"]
    return top15.groupby(["Continent", "% Renewable"])[
        "Continent"].agg(np.size).dropna()
    raise NotImplementedError()


print(answer_twelve())
assert isinstance(
    answer_twelve(), pd.Series), "Q12: You should return a Series!"
assert len(answer_twelve()) == 9, "Q12: Wrong result numbers!"
print("")

print("Question 13")


# Convert the Population Estimate series to a string with thousands separator (using commas)
# Use all significant digits (do not round the results).
# e.g. 12345678.90 -> 12,345,678.90
# This function should return a series PopEst whose index is the country
# name and whose values are the population estimate string


def answer_thirteen():
    top15 = answer_one()
    top15['Est_Pop'] = top15['Energy Supply'] / \
        top15['Energy Supply per Capita']
    return top15['Est_Pop'].apply('{0:,}'.format).astype(str)
    raise NotImplementedError()


print(answer_thirteen())
assert isinstance(answer_thirteen(),
                  pd.Series), "Q13: You should return a Series!"
assert len(answer_thirteen()) == 15, "Q13: Wrong result numbers!"
print("")

print("Optional")


def plot_optional():
    import matplotlib.pyplot as plt
    top15 = answer_one()
    ax = top15.plot(x='Rank',
                    y='% Renewable',
                    kind='scatter',
                    c=['#e41a1c',
                       '#377eb8',
                       '#e41a1c',
                       '#4daf4a',
                       '#4daf4a',
                       '#377eb8',
                       '#4daf4a',
                       '#e41a1c',
                       '#4daf4a',
                       '#e41a1c',
                       '#4daf4a',
                       '#4daf4a',
                       '#e41a1c',
                       '#dede00',
                       '#ff7f00'],
                    xticks=range(1,
                                 16),
                    s=6 * top15['2014'] / 10 ** 10,
                    alpha=.75,
                    figsize=[16,
                             6])

    for i, txt in enumerate(top15.index):
        ax.annotate(
            txt, [
                top15['Rank'][i], top15['% Renewable'][i]], ha='center')
    return plt.show()


print(plot_optional())
print(
    "This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")
