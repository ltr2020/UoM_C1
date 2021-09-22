import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
#find list of all the names
    pattern = "[A-Z][a-z]*"
    return re.findall(pattern, simple_string)
print(names())
assert len(name
s()) == 4, "There are four names in the simple_string"
#the boolean expression that checks if the statement is True or Falss
#If the statement is true then it does nothing and continues the execution
#but if the statement is False then it throws an error


#Create a regex to generate a list of just those students who received a B in the course
import re
def grades():
    with open(r"C:\Users\user\PycharmProjects\UoM\Doc\grades.txt", "r") as file:
        grades = file.read()    #read whole doc as one str
    pattern = "[\w]* [\w]*(?=: B)"    #\s = \(space)
    return re.findall(pattern, grades)
print(grades())
assert len(grades()) == 16
#or
def grades():
    with open(r"C:\Users\user\PycharmProjects\UoM\Doc\grades.txt", "r") as file:
        grades = file.read()    #read whole doc as one str
        B_names = []
    for i in re.finditer("(?P<name>.*)(: B)", grades):
        B_names.append(i.groupdict("name"))
    return B_names
print(grades())


#Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
example_dict = {"host":"146.204.224.152",
                "user_name":"feest6811",
                "time":"21/Jun/2019:15:45:24 -0700",
                "request":"POST /incentivize HTTP/1.1"}

import re
def logs():
    with open(r"C:\Users\user\PycharmProjects\UoM\Doc\logdata.txt", "r") as file:
        logdata = file.read()
    pattern = """
    (?P<host>[\d]*.[\d]*.[\d]*.[\d]*)    
    (\ -\ )  
    (?P<user_name>[\w-]*) 
    (\ \[) 
    (?P<time>\w*/\w*/.*)
    (\]\ \") 
    (?P<request>.*)
    (")
    """
    result = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())
    return result
print(logs())

assert len(logs()) == 979
one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs()