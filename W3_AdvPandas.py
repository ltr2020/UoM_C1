import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
staff_df = pd.DataFrame({"Name":["Kelly", "Sally", "James"],
                         "Role":["Director of HR", "Course liasion", "Grader"],
                         "Location":["x", "y", "z"]})
student_df = pd.DataFrame({"Name":["James", "Mike", "Sally"],
                         "School":["Business", "Law", "Engineering"],
                           "Location":["a", "b", "c"]})
print("One Merging dataframes")
staff_df = staff_df.set_index("Name")
student_df = student_df.set_index("Name")
print(staff_df)
print(student_df)
merge1 = pd.merge(staff_df, student_df, how="outer", on="Name")  #use index both df have as index
print(merge1)
merge2 = pd.merge(staff_df, student_df, how="inner", left_index=True, right_index=True)
print(merge2)
merge3 = pd.merge(staff_df, student_df, how="left", left_index=True, right_index=True)
print(merge3)
merge4 = pd.merge(staff_df, student_df, how="right", left_index=True, right_index=True)
print(merge4)
print(len(merge4))
print("")

print("OneA Merging datasets")
print("pd.concat([df1, df2, df3]")
print("")

print("TwoA - Chaining")
df = pd.read_csv('Doc\census.csv')
df1 = (df.where(df['SUMLEV']==50)
      .dropna()
      .set_index(['STNAME', 'CTYNAME'])
      .rename(columns={"ESTIMATESBASE2010":'EstBase2010'}))
print(df1.head())
print("or, much faster but less readability")
df2 = (df[df["SUMLEV"]==50]
       .set_index(['STNAME', 'CTYNAME'])
       .rename(columns={"ESTIMATESBASE2010":'EstBase2010'}))
print(df2.head())
print("")

print("TwoB - .aaply & lambda to add new columns")
def min_max(row):
    data = row[["POPESTIMATE2010",
               "POPESTIMATE2011",
               "POPESTIMATE2012",
               "POPESTIMATE2013",
               "POPESTIMATE2014",
               "POPESTIMATE2015"
               ]]
    row["MAX"] = np.max(data)
    row["MIN"] = np.min(data)
    return row
df_min_max = df.apply(min_max, axis="columns").head()
print("")

row = ["POPESTIMATE2010",
       "POPESTIMATE2011",
       "POPESTIMATE2012",
       "POPESTIMATE2013",
       "POPESTIMATE2014",
       "POPESTIMATE2015"]
df_min_max2 = df.apply(lambda x: [np.max(x[row]), np.min(x[row])], axis="columns").head()
print("")

print(df["STNAME"].tolist())
def Country(x):
    USA = df["STNAME"].tolist()
    if x in USA:
        return "USA"
df["Country"] = df["STNAME"].apply(lambda x: Country(x))    #create new column
print(df[["STNAME","Country"]])
del df["Country"]
print("")

print("TwoC - groupby() to split df into chunks to speed up")
def method_slow():
    for state in df["STNAME"].unique():
        avg = np.average(df[df["STNAME"]==state].dropna()["CENSUS2010POP"])
        return("Counties in state " + state + " have an avg pop of " + str(avg))

def method_fast():
    for group, frame in df.groupby("STNAME"):   ##pass a column to groupby(), o/w default index
        avg = np.average(frame["CENSUS2010POP"])
        return("Counties in state " + state + " have an avg pop of " + str(avg))
print("")

#Advanced groupby()
df= pd.read_csv("Doc/listings.csv")
print(df.head())
df=df.set_index(["cancellation_policy","review_scores_value"])
for group, frame in df.groupby(level=(0,1)):
    print(group)
print("")
# group by the cancelation policy and review scores, but
# separate out all the 10's from those under ten

def grouping_fun(item):
    if item[1] == 10.0:
        return (item[0], "10.0")
    else:
        return (item[0], "not 10.0")
for group, frame in df.groupby(by=grouping_fun):
    print(group)
print("")

print("Three Applications")
print("3-1: .agg() of data")
df=df.reset_index()
df.groupby("cancellation_policy").agg({"review_scores_value":np.average})   #doesn't work as np.avg doesn't ignore NaNs
# First we're doing a group by on the dataframe object by the column "cancellation_policy"
# Then we are invoking the agg() function on that object. The agg function is going to apply one or more
# functions we specify to the group dataframes and return a single value per column, so one row per grp
print(df.groupby("cancellation_policy").agg({"review_scores_value":(np.nanmean,np.nanstd),
                                      "reviews_per_month":np.nanmean}))
print("")
print("3-2: .transform() of data")
# unlike agg(), tranform() returns an object that is the same size as the group,
# returning a new dataframe. This makes combining data later easy
# we want to include the average rating values in a given group by cancellation policy,
# but preserve the dataframe shape so that we could generate a difference
# between an individual observation and the sum.

# First, lets define just some subset of columns we are interested in
cols=['cancellation_policy','review_scores_value']
# Now lets transform it, I'll store this in its own dataframe
transform_df=df[cols].groupby('cancellation_policy').transform(np.nanmean)
print(transform_df.head())
# So we can see that the index here is actually the same as the original dataframe. So lets just join this
# in. Before we do that, lets rename the column in the transformed version
transform_df.rename({'review_scores_value':'mean_review_scores'}, axis='columns', inplace=True)
print(transform_df.head())
df=df.merge(transform_df, left_index=True, right_index=True)
print(df.head())
# Great, we can see that our new column is in place, the mean_review_scores. So now we could create, for
# instance, the difference between a given row and it's group (the cancellation policy) means.
df['mean_diff']=np.absolute(df['review_scores_value']-df['mean_review_scores'])
print(df['mean_diff'].head())
print("")

print("Faster approach: .aaply()")
# In previous work we wanted to find the average review score of a listing and its deviation from the group
# mean. This was a two step process, first we used transform() on the groupby object and then we had to
# broadcast to create a new column. With apply() we could wrap this logic in one place
def calc_mean_review_scores(group):
    # group is a dataframe just of whatever we have grouped by, e.g. cancellation policy, so we can treat
    # this as the complete dataframe
    avg=np.nanmean(group["review_scores_value"])
    # now broadcast our formula and create a new column
    group["review_scores_mean"]=np.abs(avg-group["review_scores_value"])
    return group
print("")

# Now just apply this to the groups
df.groupby('cancellation_policy').apply(calc_mean_review_scores).head()

print("3-3: filter of data")
# often that you'll want to groupby some feature, then make some transformation to the groups,
# then drop certain groups as part of your cleaning routines
# The filter() function takes in a function which it applies to each group dataframe and
# returns either a True or a False to be included in the grp

df.groupby('cancellation_policy').filter(lambda x: np.nanmean(x['review_scores_value'])>9.2)

