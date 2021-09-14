import re
text = 'it is on me, or on someone else'
x = re.findall('on', text)  # returns a list containing all matches
print(x)
y = re.search('me', text)
print(y)    # reMatch object, tells you boolean, location and matching word
print(y.group())
z = re.match('^it', text)    #only the first word
print(z.span())

pattern = re.compile(r'\S')
x = pattern.search('I don\'t know what \s is') #/s = space or tab
print(x.start())

#"^abc..." check if 'start' with particular pattern
#"abc...$" check if 'end' with ...
#"abc|cde" check either/or contain abc or cde

grades = 'ACAAAABCBCBAA'
print(re.findall(r'[A][B-C]', grades))
print(re.findall(r'[A-B][C]', grades))
print(re.findall(r'[^A]', grades))  #[^A] to negate words = match non-A
print(re.findall(r'^[^A]', grades))  #match bgn of strong with non-A
