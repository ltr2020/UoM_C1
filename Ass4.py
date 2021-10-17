import re
import scipy.stats as stats
import numpy as np
import pandas as pd

# Remember that to calculate the correlation with pearsonr
# so you are going to send in two ordered lists of values, the populations from the wikipedia_data.html file
# and the win/loss ratio for a given sport in the same order
# Average the win/loss ratios for those cities which have multiple teams
# of a single sport

print("Question 1")
# Calculate the win/loss ratio's correlation with the population of
# the city it is in for the NHL using 2018 data

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)


def nhl_correlation():
    # YOUR CODE HERE
    nhl_df = pd.read_csv("Doc/nhl.csv")
    nhl_df = nhl_df[nhl_df["year"] == 2018]  # filter 2018
    nhl_df = nhl_df[["team", "W", "L"]]  # filter team name and W/L
    nhl_df["team"] = nhl_df["team"].str.replace(
        r"\*", "", regex=True)  # remove "*" in team name
    # filter out city name to leave only team names
    nhl_df["team_only"] = nhl_df["team"].apply(lambda x: x.split()[-1])

    # manually correct names
    nhl_df.iloc[3, 3] = "Maple Leafs"
    nhl_df.iloc[5, 3] = "Red Wings"
    nhl_df.iloc[13, 3] = "Blue Jackets"
    nhl_df.iloc[27, 3] = "Golden Knights"

    # from NYC
    nhl_df.iloc[14, 3] = "RangersIslandersDevils"
    nhl_df.iloc[16, 3] = "RangersIslandersDevils"
    nhl_df.iloc[17, 3] = "RangersIslandersDevils"

    # from LA
    nhl_df.iloc[28, 3] = "KingsDucks"
    nhl_df.iloc[30, 3] = "KingsDucks"

    cities = pd.read_html("Doc/wikipedia_data.html")[1]
    cities = cities.iloc[: -1, [0, 3, 8]]
    cities["NHL"] = cities["NHL"].str.replace(
        "\\[[\\w\\s]*\\]", "", regex=True)
    cities.rename(columns={"Metropolitan area": "City",
                           "Population (2016 est.)[8]": "Population",
                           "NHL": "team_only"},
                  inplace=True)  # change column name

    merged = pd.merge(nhl_df, cities, how="inner", on="team_only")
    merged.W = merged.W.astype(float)
    merged.L = merged.L.astype(float)
    merged.Population = merged.Population.astype(float)
    merged["W/L%"] = merged["W"] / (merged["W"] + merged["L"])
    merged = merged.groupby("City")[["W/L%", "Population"]].agg(np.nanmean)

    population_by_region = merged["Population"]
    win_loss_by_region = merged["W/L%"]

    assert len(population_by_region) == len(
        win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(
        population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]
    raise NotImplementedError()


print(nhl_correlation())
print("")
print("Question 2")
# win/loss ratio's correlation with the population of the city
# for the NBA using 2018 data


def nba_correlation():
    nba_df = pd.read_csv("Doc/nba.csv")
    nba_df.iloc[1, 8] = 2018
    nba_df.iloc[17, 8] = 2018
    nba_df = nba_df[nba_df["year"] == 2018]  # filter 2018
    nba_df = nba_df[["team", "W", "L"]]  # filter team name and W/L
    nba_df["team"] = nba_df["team"].str.replace(
        r"[\*]*", "", regex=True)  # leave only team name
    nba_df["team"] = nba_df["team"].str.replace(
        r"[\xa0]", "", regex=True)  # leave only team name
    nba_df["team"] = nba_df["team"].str.replace(
        r"\(\d*\)]*", "", regex=True)  # leave only team name
    # filter out city name to leave only team names
    nba_df["team_only"] = nba_df["team"].apply(lambda x: x.split()[-1])

    # manually correct names
    nba_df.loc[17, "team_only"] = "Trail Blazers"

    nba_df.loc[10, "team_only"] = "KnicksNets"
    nba_df.loc[11, "team_only"] = "KnicksNets"

    nba_df.loc[24, "team_only"] = "LakersClippers"
    nba_df.loc[25, "team_only"] = "LakersClippers"

    cities = pd.read_html("Doc/wikipedia_data.html")[1]
    cities = cities.iloc[: -1, [0, 3, 7]]
    cities["NBA"] = cities["NBA"].str.replace(
        "\\[[\\w\\s]*\\]", "", regex=True)
    cities.rename(columns={"Metropolitan area": "City",
                           "Population (2016 est.)[8]": "Population",
                           "NBA": "team_only"},
                  inplace=True)  # change column name

    merged = pd.merge(nba_df, cities, how="inner", on="team_only")
    merged.W = merged.W.astype(float)
    merged.L = merged.L.astype(float)
    merged.Population = merged.Population.astype(float)
    merged["W/L%"] = merged["W"] / (merged["W"] + merged["L"])
    merged = merged.groupby("City")[["W/L%", "Population"]].agg(np.nanmean)

    population_by_region = merged["Population"]
    win_loss_by_region = merged["W/L%"]

    assert len(population_by_region) == len(
        win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(
        population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]
    raise NotImplementedError()


print(nba_correlation())

print("Question 3")
# calculate the win/loss ratio's correlation with the population of the city
# for the MLB using 2018 data


def mlb_correlation():
    # YOUR CODE HERE
    mlb_df = pd.read_csv("Doc/mlb.csv")
    mlb_df = mlb_df[mlb_df["year"] == 2018]  # filter 2018
    mlb_df = mlb_df[["team", "W", "L"]]  # filter team name and W/L
    # filter out city name to leave only team names
    mlb_df["team_only"] = mlb_df["team"].apply(lambda x: x.split()[-1])

    # manually correct names
    mlb_df.loc[0, "team_only"] = "Red Sox"
    mlb_df.loc[3, "team_only"] = "Blue Jays"
    mlb_df.loc[8, "team_only"] = "CubsWhite Sox"

    mlb_df.loc[1, "team_only"] = "YankeesMets"
    mlb_df.loc[18, "team_only"] = "YankeesMets"

    mlb_df.loc[13, "team_only"] = "DodgersAngels"
    mlb_df.loc[25, "team_only"] = "DodgersAngels"

    mlb_df.loc[21, "team_only"] = "CubsWhite Sox"

    mlb_df.loc[11, "team_only"] = "GiantsAthletics"
    mlb_df.loc[28, "team_only"] = "GiantsAthletics"

    cities = pd.read_html("Doc/wikipedia_data.html")[1]
    cities = cities.iloc[: -1, [0, 3, 6]]
    cities["MLB"] = cities["MLB"].str.replace(
        "\\[[\\w\\s]*\\]", "", regex=True)
    cities.rename(columns={"Metropolitan area": "City",
                           "Population (2016 est.)[8]": "Population",
                           "MLB": "team_only"},
                  inplace=True)  # change column name

    merged = pd.merge(mlb_df, cities, how="inner", on="team_only")
    merged.W = merged.W.astype(float)
    merged.L = merged.L.astype(float)
    merged.Population = merged.Population.astype(float)
    merged["W/L%"] = merged["W"] / (merged["W"] + merged["L"])
    merged = merged.groupby("City")[["W/L%", "Population"]].agg(np.nanmean)

    population_by_region = merged["Population"]
    win_loss_by_region = merged["W/L%"]

    assert len(population_by_region) == len(
        win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(
        population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]
    raise NotImplementedError()
print(mlb_correlation())

print("Question 4")
# calculate the win/loss ratio's correlation with the population of the city
# for the NFL using 2018 data
def nfl_correlation():
    nfl_df = pd.read_csv("Doc/nfl.csv")
    nfl_df = nfl_df[nfl_df.year == 2018]
    nfl_df = nfl_df.loc[:, ["L", "W", "team"]]
    nfl_df.team = nfl_df["team"].str.replace(r"[\*\+]*", "", regex=True)
    nfl_df = nfl_df[~nfl_df.team.str.contains(
        "|".join(["AFC", "NFC"]))].reset_index()  # remove unnecessary parts
    del nfl_df["index"]
    # filter out city name to leave only team names
    nfl_df["team_only"] = nfl_df["team"].apply(lambda x: x.split()[-1])

    # manually correct names
    nfl_df.loc[3, "team_only"] = "GiantsJets"
    nfl_df.loc[19, "team_only"] = "GiantsJets"
    nfl_df.loc[13, "team_only"] = "RamsChargers"
    nfl_df.loc[28, "team_only"] = "RamsChargers"
    nfl_df.loc[30, "team_only"] = "49ersRaiders"
    nfl_df.loc[15, "team_only"] = "49ersRaiders"

    cities = pd.read_html("Doc/wikipedia_data.html")[1]
    cities = cities.iloc[: -1, [0, 3, 5]]
    cities["NFL"] = cities["NFL"].str.replace("\\[[\\w\\s]*\\]", "", regex=True)
    cities.rename(columns={"Metropolitan area": "City",
                           "Population (2016 est.)[8]": "Population",
                           "NFL": "team_only"},
                  inplace=True)  # change column name

    merged = pd.merge(nfl_df, cities,
                      how="inner",
                      on="team_only")

    merged.W = merged.W.astype(float)
    merged.L = merged.L.astype(float)
    merged.Population = merged.Population.astype(float)
    merged["W/L%"] = merged["W"] / (merged["W"] + merged["L"])
    merged = merged.groupby(
        "City")[["W/L%", "Population"]].agg(np.nanmean).reset_index()

    population_by_region = merged["Population"]
    win_loss_by_region = merged["W/L%"]

    assert len(population_by_region) == len(
        win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(
        population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"

    return stats.pearsonr(population_by_region, win_loss_by_region)[0]
print(nfl_correlation())