import pandas as pd
import numpy as np
# 4 main time related classes. Timestamp, DatetimeIndex, Period, and PeriodIndex

# Timestamp is interchangeable with Python's datetime in most cases
print("TIMESTAMP: single pt in time")
day = pd.Timestamp('2019-9-1 10:05:08AM')
#or
print(pd.to_datetime('4/7/12', dayfirst=True))
# or
print(pd.Timestamp(2019, 9, 1, 10, 5, 8))
# Timestamp also has some useful attributes, such as isoweekday(), which shows the weekday of the timestamp
# note that 1 represents Monday and 7 represents Sunday
print(pd.Timestamp(day).isoweekday())
# You can find extract the specific year, month, day, hour, minute, second from a timestamp
print(pd.Timestamp(day).second)
print("")

print("PERIOD")
print(pd.Period('1/2016') + 5)
print(pd.Period('3/5/2016') - 2)
print("")

print("Timedelta: diff in time")
print(pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016'))
print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))
print("")

print("Offset: similar to timedelta but fixed time intervals i.e. hr, day, biz day, end of mth, semi mth bgn, etc.")
pd.Timestamp('9/4/2016').weekday()
pd.Timestamp('9/4/2016') + pd.offsets.BusinessDay()
pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd()
print("")

print("DatatimeIndex & PeriodIndex")
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'),
                             pd.Timestamp('2016-09-03')])
print(t1)
print(type(t1.index))
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'),
                             pd.Period('2016-11')])
print(t2)
print(type(t2.index))
print("")

print("Convert to Datetime")
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1,
                   columns=list('ab'))
print(ts3)
ts3.index = pd.to_datetime(ts3.index)
print(ts3)
print("")

print("Working with Dates in a Dataframe")
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
print(df)
print(df.index.weekday)    #check what day for each date
print(df.diff)  #diff of value(s) b/w each date
print(df.resample('M').mean())  #want to know the mean value for each month (downsampling)
print("")
#slicing
print(df.loc["2016-12"])