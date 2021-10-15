import re
import scipy.stats as stats
import numpy as np
import pandas as pd
print("Question 1")
# Calculate the win/loss ratio's correlation with the population of
# the city it is in for the NHL using 2018 data

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)

nhl_df = pd.read_csv("Doc/nhl.csv")
cities = pd.read_html("Doc/wikipedia_data.html")[1]
cities = cities.iloc[:-1, [0, 3, 5, 6, 7, 8]]
print(cities)


def nhl_correlation():
    # YOUR CODE HERE
    nhl_df = nhl_df[nhl_df[year] == 2018]
    pd.to_excel
    raise NotImplementedError()

    population_by_region = []  # pass in metropolitan area population from cities
    # pass in win/loss ratio from nhl_df in the same order as
    # cities["Metropolitan area"]
    win_loss_by_region = []

    assert len(population_by_region) == len(
        win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(
        population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"

    return stats.pearsonr(population_by_region, win_loss_by_region)
