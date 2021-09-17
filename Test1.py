import re
text = 'it is on me, or on someone else'
x = re.findall('on', text)  # returns a list containing all matches
print(x)
y = re.search('on', text)
print(y)    # reMatch object, tells you boolean, location and matching word
print(y.group(0))
z = re.match('^it', text)    #only the first word
print(z.span())
a = re.split(",", text)
print(a)

pattern = re.compile(r'\s{1}')  #another method
x = pattern.search('I don\'t know what \s is') #/s = space or tab
print('\n', x.start())

#"^abc..." check if 'start' with particular pattern
#"abc...$" check if 'end' with ...
#"abc|cde" check either/or contain abc or cde
#[\d]* = 0 or more instances of the preceding regex token, see ass_1
# ?: Match expression but do not capture it.
# ?= Match a suffix but exclude it from capture.
# ?! = look ahead, Match if the suffix is absent
# ?P<name> labels group as dictinary so that you can recall later with item.groupdict()
# * to means zero or more times e.g.[\w]{1,100} = [\w]*
# + = 1 or more
# search() & match()  returns return individual match
# findall() returns string
# finditer() returns a tuple for each match
grades = 'ACAAAABCBCBAA'
print(re.findall(r'[A][B-C]', grades))  #A and B or C combo
print(re.findall(r'[A-B][C]', grades))
print(re.findall(r'[^A]', grades))  #[^A] to negate words = match non-A
print(re.findall(r'^[^B]', grades))  #match bgn of strong with non-B
print(re.findall(r'A{1,2}', grades))  #match A or AA
print(re.findall(r'...', grades))       #match 3 characters


#verbose mode of regex, much easier to read for multiple regexes

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