# (x, y, z) tuples are immutable
# [x, y, z] lists are mutable i.e. can be altered and appended

# Adv string op & Dictionaries
import re
import time as tm
import datetime as dt
sales_record = {'price': 3.24,
                'num_items': 4,
                'person': 'Chris'}
sales_record["date"] = "01/09/2021"  # add/change item
del sales_record["date"]  # delete or sales_record.clear() to clear all
print(sales_record["price"])
print(sales_record.get("price"))  # or
for i in sales_record:
    print(i)  # only show key
for i in sales_record.items():  # return a tuple containing Key and Value
    print(i)
print("")


sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(
    sales_statement.format(
        sales_record['person'],
        sales_record['num_items'],
        sales_record['price'],
        sales_record['num_items'] *
        sales_record['price']))

# Class function


class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

    def deposit(self, amount):  # 存款動作: amount代表存入金額
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount

    def withdraw(self, amount):  # 取款動作: amount代表取款金額
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')


acct1 = Account("123-456-789", "Justin")
acct1.deposit(100)
acct1.withdraw(30)
print(acct1.balance)  # 餘額是 70

# Lambda


def my_function(a, b, c): return a + b


a = my_function(1, 2, 3)
print("\n", a)

# List comprehensions: to create a new list based on the values of an
# existing list
my_list = [x for x in range(0, 20) if x % 2 == 0]
print(my_list)

# eqivalent to
list1 = range(0, 20)
list2 = []
for x in list1:
    if x % 2 == 0:
        list2.append(x)

# same as
my_list = []
for number in range(0, 20):
    if number % 2 == 0:
        my_list.append(number)
my_list

#Date and Time

tm.time()  # time in sec since 1/1/1970

dtnow = dt.datetime.fromtimestamp(tm.time())  # convert timestamp to datetime
print(dtnow)

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
# get year, month, day, etc.from a datetime

delta = dt.timedelta(days=100)  # create a timedelta of 100 days
print(delta)

# Regex
text = 'it is on me, or on someone else'
x = re.findall('on', text) # returns a list containing all matches
print(x)
y = re.search('on', text)
print(y)    # reMatch object, tells you boolean, location and matching word
print(y.group(0))
z = re.match('^it', text)  # only the first word
print(z.span())
a = re.split(",", text)
print(a)
pattern = re.compile(r'\s{1}')  # another method
x = pattern.search('I don\'t know what \\s is')  # /s = space or tab
print('\n', x.start())

# "^abc..." check if 'start' with particular pattern
# "abc...$" check if 'end' with ...
# "abc|cde" check either/or contain abc or cde
# [\d]* = 0 or more instances of the preceding regex token, see ass_1
# (?:) for non capturing group
#       a(?:b) will match the "ab" in "abc", while a(?=b) will only match the "a" in "abc"
# (?=) for positive look ahead.
#       a(?=b) will match the "a" in "ab", but not the "a" in "ac"
# (?!) for negative look ahead
#       a(?!b) will match the "a" in "ac", but not the "a" in "ab".
# (?<=) for positive look behind
# (?<!) for negative look behind
# (?P<name>) labels group as dictionary so that you can recall later with item.groupdict()
# * to means zero or more times e.g.[\w]{1,100} = [\w]*
# + = 1 or more
# search() & match()  returns return individual match
# findall() returns string
# finditer() returns a tuple for each match
grades = 'ACAAAABCBCBAA'
print(re.findall(r'[A][B-C]', grades))  # A and B or C combo
print(re.findall(r'[A-B][C]', grades))
print(re.findall(r'[^A]', grades))  # [^A] to negate words = match non-A
print(re.findall(r'^[^B]', grades))  # match bgn of strong with non-B
print(re.findall(r'A{1,2}', grades))  # match A or AA
print(re.findall(r'...', grades))  # match 3 characters


# verbose mode of regex, much easier to read for multiple regexes

# Without Using VERBOSE
regex_email = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2, 6})$',
                         re.IGNORECASE)

# Using VERBOSE
regex_email = re.compile(r"""
            ^([a-z0-9_\.-]+)              # local Part
            @                             # single @ sign
            ([0-9a-z\.-]+)                # Domain name
            \.                            # single Dot .
            ([a-z]{2,6})$                 # Top level Domain
             """, re.VERBOSE | re.IGNORECASE)
