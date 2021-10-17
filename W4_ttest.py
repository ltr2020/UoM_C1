from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
print("1: Basic Stats Testing")
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)
df = pd.read_csv('Doc/grades.csv')
print(f"There are {df.shape[0]} rows and {df.shape[1]} columns")

# segment this population into two pieces
# Let's say those who finish the first assignment by the end of December 2015, we'll call them early finishers,
# and those who finish it sometime after that, we'll call them late finishers.

early_finishers = df[pd.to_datetime(df['assignment1_submission']) < '2016']
late_finishers = df[pd.to_datetime(df['assignment1_submission']) >= '2016']
# or late_finishers2= df[~df.index.isin(early_finishers.index)]  #~ =
# negation operation
print(early_finishers['assignment1_grade'].mean())
print(late_finishers['assignment1_grade'].mean())
print("1-1: T-test")
# SciPy library for hypothesis testing
# ttest_ind() for independent t-test (pop not related to one another
# The result: t-statistic and a p-value.
# p-value < alpha --> stat sig alt hypothesis (means of wo pops diff)
print(
    ttest_ind(
        early_finishers['assignment1_grade'],
        late_finishers['assignment1_grade']))
print(
    ttest_ind(
        early_finishers['assignment2_grade'],
        late_finishers['assignment2_grade']))
print(
    ttest_ind(
        early_finishers['assignment3_grade'],
        late_finishers['assignment3_grade']))
print(
    ttest_ind(
        early_finishers['assignment4_grade'],
        late_finishers['assignment4_grade']))
print(
    ttest_ind(
        early_finishers['assignment5_grade'],
        late_finishers['assignment5_grade']))
print(
    ttest_ind(
        early_finishers['assignment6_grade'],
        late_finishers['assignment6_grade']))
# p-values insig to reject null hypothesis
# but still can be informative
# E.g. p-value for assignment 3 around 0.1
# If we use alpha =0.11 this would have been considered stat sig
# As a research, this would suggest to me that there is something here
# worth considering following up on
print("")

print("1-2: CI & Baysian Analysis")
# P-values under fire recently for being insuff
# confidence intervalues and bayesian analyses, are being used more regularly
# One issue with p-values is that as you run more tests likely to get a value which
# is statistically significant just by chance.
# list comprehension to create 100x100 df, without it only 1x100
df1 = pd.DataFrame([np.random.random(100) for i in range(100)])
df2 = pd.DataFrame([np.random.random(100) for i in range(100)])


def test_columns(alpha=0.1):
    # I want to keep track of how many differ
    num_diff = 0
    # And now we can just iterate over the columns
    for x in df1.columns:
        # we can run out ttest_ind between the two dataframes
        ttstat, pval = ttest_ind(df1[x], df2[x])
        # and we check the pvalue versus the alpha
        if pval <= alpha:
            # And now we'll just print out if they are different and increment
            # the num_diff
            print(
                f"Col {x} is statistically significantly different at alpha={alpha}, pval={pval}"
                    )
            num_diff += 1
    # and let's print out some summary stats
    print(f"Total number different was {num_diff}, which is {float(num_diff) / len(df1.columns) * 100}%")


# And now lets actually run this
test_columns()
# all the ttest does is check if two sets are similar given some level of confidence
# he more random comparisons you do, the more will just happen to be the same by chance
# In this example, ~10%(13) of them if our alpha was 0.1.
print("")

# try alpha=5%
test_columns(0.05)

df2 = pd.DataFrame([np.random.chisquare(df=1, size=100) for i in range(100)])
test_columns()
print(df2.head())
