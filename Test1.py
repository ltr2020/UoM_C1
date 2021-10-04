import numpy as np
import pandas as pd

df= pd.read_csv("Doc/listings.csv")
df.groupby("cancellation_policy").agg({"review_scores_value":np.average})   #doesn't work as np.avg doesn't ignore NaNs
# First we're doing a group by on the dataframe object by the column "cancellation_policy"
# Then we are invoking the agg() function on that object. The agg function is going to apply one or more
# functions we specify to the group dataframes and return a single row per dataframe/group
print(df.groupby("cancellation_policy").agg({"review_scores_value":(np.nanmean,np.nanstd),
                                      "reviews_per_month":np.nanmean}))
