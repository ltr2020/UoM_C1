import re
import pandas as pd
print("Question 1")


def names():
    simple_string = "Amy is 5 years old, and her sister Mary is 2 years old." \
                    "Ruth and Peter, their parents, have 3 kids."
# find list of all the names
    pattern = "[A-Z][a-z]*"
    return re.findall(pattern, simple_string)


print(names())
assert len(names()) == 4, "There are four names in the simple_string"
# assert function, if the statement is False then it throws an error
print("")
print("Question 2")
# Create a regex to generate a list of just those students who received a
# B in the course


def grades():
    with open("Doc\\grades.txt", "r") as file:
        grades = file.read()  # read whole doc as one str
    pattern = "[\\w]* [\\w]*" \
              "(?=: B)"  # \s = \(space)
    return re.findall(pattern, grades)


print(grades())
print("")
assert len(grades()) == 16
# or


def grades():
    with open("Doc\\grades.txt", "r") as file:
        grades = file.read()  # read whole doc as one str
        B_names = []
    for i in re.finditer("[\\w]* [\\w]* (?=: B)",
                         grades):  # memory efficient to use re.finditer
        B_names.append(i.group())
    return B_names


print(grades())

print("")
print("Question 3")
# Your task is to convert this into a list of dictionaries, where each
# dictionary looks like the following:
example_dict = {"host": "146.204.224.152",
                "user_name": "feest6811",
                "time": "21/Jun/2019:15:45:24 -0700",
                "request": "POST /incentivize HTTP/1.1"}


def logs():
    with open("Doc\\logdata.txt", "r") as file:
        logdata = file.read()
    pattern = """
    (?P<host>\\d*.\\d*.\\d*.\\d*)
    (\\ -\\ )
    (?P<user_name>[\\w-]*)
    (\\ \\[)
    (?P<time>\\w*/\\w*/.*)
    (\\]\\ \")
    (?P<request>.*)
    (")
    """
    result = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())
    return result


print(logs())

assert len(logs()) == 979
one_item = {'host': '146.204.224.152',
            'user_name': 'feest6811',
            'time': '21/Jun/2019:15:45:24 -0700',
            'request': b'POST /incentivize HTTP/1.1'}
assert one_item in logs()
