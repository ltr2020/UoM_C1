#(x, y, z) tuples are immutable
#[x, y, z] lists are mutable i.e. can be altered and appended

#Adv string op & Dictionaries
sales_record = {'price': 3.24,
                'num_items': 4,
                'person': 'Chris'}
sales_record["date"] = "01/09/2021"     #add/change item
del sales_record["date"]                #delete or sales_record.clear() to clear all
print(sales_record["price"])
print(sales_record.get("price"))    #or
for i in sales_record:
    print(i)        #only show key
for i in sales_record.items():  #return a tuple containing Key and Value
    print(i)



sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print("\n", sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

#Class function
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
print(acct1.balance) #餘額是 70

#Lambda
my_function = lambda a, b, c : a + b
a = my_function(1, 2, 3)
print("\n", a)

#List comprehensions
my_list = [number for number in range(0,20) if number % 2 == 0]
print(my_list)

#same as
my_list = []
for number in range(0, 20):
    if number % 2 == 0:
        my_list.append(number)
my_list

#Date and Time
import datetime as dt
import time as tm

tm.time()   #time in sec since 1/1/1970

dtnow = dt.datetime.fromtimestamp(tm.time())    #convert timestamp to datetime
print(dtnow)

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
# get year, month, day, etc.from a datetime

delta = dt.timedelta(days = 100) # create a timedelta of 100 days
print(delta)

