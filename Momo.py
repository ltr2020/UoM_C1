import pandas as pd
import numpy as np
df = pd.read_csv('Doc/cwurData.csv')
print(df.head())
print("")

def create_category(ranking):
    if (ranking >= 1) & (ranking <= 100):
        return "First Tier Top Unversity"
    elif (ranking >= 101) & (ranking <= 200):
        return "Second Tier Top Unversity"
    elif (ranking >= 201) & (ranking <= 300):
        return "Third Tier Top Unversity"
    return "Other Top Unversity"
df['Rank_Level'] = df['world_rank'].apply(lambda x: create_category(x))
print(df.head())
print("")

# A pivot table allows us to pivot out one of these columns a new column headers and compare it against
# another column as row indices. Let's say we want to compare rank level versus country of the universities
# and we want to compare in terms of overall score
# aren't limited to one function that you might want to apply. aggfunc, a list of the different functions

print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max]).head())
# overall average for the country and max of the max-->  marginal values
print("")
print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max],
                     margins=True).head())
print("")
print("")

# A pivot table is just a multi-level dataframe, and we can access series or cells in the dataframe in a similar way
# as we do so for a regular dataframe.
# Let's create a new dataframe from our previous example
new_df=df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max],
               margins=True)
# Now let's look at the index
print(new_df.index)
print("")
# And let's look at the columns
print(new_df.columns)
# olumns are hierarchical. The top level column indices have two categories: mean and max,
# the lower level column indices have four categories, which are the four rank levels

# How would we query this if we want to get the average scores of First Tier Top Unversity levels in each country? We would just need
# to make two dataframe projections, the first for the mean, then the second for the top tier
print(new_df['mean']['First Tier Top Unversity'].head())
# We can see that the output is a series object which we can confirm by printing the type. Remember that when
# you project a single column of values out of a DataFrame you get a series.
print(type(new_df['mean']['First Tier Top Unversity']))
# find the country that has the maximum average score on First Tier Top University level?
# use the idxmax() function
print(new_df['mean']['First Tier Top Unversity'].idxmax())
print("")
print("")

# If you want to achieve a different shape of your pivot table, you can do so with the stack and unstack
# functions. Stacking is pivoting the lowermost column index to become the innermost row index. Unstacking is
# the inverse of stacking, pivoting the innermost row index to become the lowermost column index. An example
# will help make this clear

# Let's look at our pivot table first to refresh what it looks like
print(new_df.head())
# Now let's try stacking, this should move the lowermost column, so the tiers of the university rankings, to
# the inner most row
print("STACK")
new_df=new_df.stack()
print(new_df.head())
# In the original pivot table, rank levels are the lowermost column, after stacking, rank levels become the
# innermost index, appearing to the right after country

# Now let's try unstacking
new_df.unstack().head()
# That seems to restore our dataframe to its original shape. What do you think would happen if we unstacked twice in a row?
print("UNSTACK")
print(new_df.unstack().unstack().head())
# We actually end up unstacking all the way to just a single column, so a series object is returned. This
# column is just a "value", the meaning of which is denoted by the heirarachical index of operation, rank, and
# country.