#NumPy
import numpy as np
a = np.array([[1,2.5,3], [4,5.8,6], [7,8,9]]) #float / int
print(a)
print(a[:,(0,2)])   #all row and 1th and 3rd column
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a @ a) #dot product
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())

b = np.zeros((2,3))
print("\n",b)
c = np.ones((3,3))
print("\n",c)
d = np.random.rand(5,2) #just single bracket
print("\n",d)
e = np.arange(2,50,2).reshape(6,4) #3rd arg is interval b/w no
print("\n",e)
f = np.linspace(2,3,5) #3rd arg is the no of items
print("\n",f)

print("\n")
temp = np.array([-15, 23, 4, 5, 18, 12])
print(temp < 20)

#Matrix slicing
a = np.array([[1,2],
               [3,4],
               [5,6]])
print('\n',a)
print(np.array([a[0,0], a[1,1], a[2,1]]))
print(a[[0,1,2], [0,1,1]])  #all row selected & J10, J11, J21 selected
print(a>4)  #Boolean indexing
print(a[a>4])


#PIL image processing
from PIL import Image   #Pycham somehow can't install PIL
im = Image.open(r'C:\Users\lokti\PycharmProjects\UoM_C1\Doc\Messi.jpg')
im.show()
print(im.format, im.mode)
import numpy as np
array = np.array(im)    #convert PIL mage to numpy array
print("\n", array.shape)
print("\n", array)    #200x200 array with all values = unit8 up to bites per byte(2**8=) 256 in size
array2D = array.reshape(1467,6603)  #3D to 2D
print("\n", array2D.shape)
print("\n", array2D)
mask = np.full(array2D.shape,255) #same shape but all var = 255 (white)
print("\n", mask)
modified_array = array2D - mask
print(modified_array)
modified_array -= 1 #convert all negative to positive
modified_array = modified_array.astype(np.uint8)    #tell np to set the value of datatype correctly
print(modified_array.shape)
print(modified_array)
inverted = Image.fromarray(modified_array)
inverted.show() #B&W inverted image but dimension changed

#Reading and writing CSV
# mpg : miles per gallon
# class : car classification
# cty : city mpg
# cyl : # of cylinders
# displ : engine displacement in liters
# drv : f = front-wheel drive, r = rear wheel drive, 4 = 4wd
# fl : fuel (e = ethanol E85, d = diesel, r = regular, p = premium, c = CNG)
# hwy : highway mpg
# manufacturer : automobile manufacturer
# model : model of car
# trans : type of transmission
# year : model year
import csv
with open(r'Doc/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile)) #`csv.Dictreader`read each row as a dictionary.
print("\n")
print(mpg[:3]) # The first three s = dictionaries in our list
print(len(mpg))    #234 dictionaries = 234 cars
print(mpg[1].keys())   #`keys` gives us the column names of our csv
print(sum(float(i['cty']) for i in mpg) / len(mpg))    #average cty fuel economy across all cars. All values in the dictionaries are strings, so we need to convert to float
print(sum(float(i['hwy']) for i in mpg) / len(mpg))


cylinders = set(i['cyl'] for i in mpg)  #find unique values of the key
print(cylinders)
# grouping the cars by number of cylinder
# finding the average cty mpg for each group.
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for i in mpg: # iterate over all dictionaries
        if i['cyl'] == c: # if the cylinder level type matches,
            summpg += float(i['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)

vehicleclass = set(i['class'] for i in mpg) # what are the class types
print(vehicleclass)
HwyMpgByClass = []
for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for i in mpg: # iterate over all dictionaries
        if i['class'] == t: # if the cylinder amount type matches,
            summpg += float(i['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[0])
print(HwyMpgByClass)

#Another example
wines = np.genfromtxt('datasets/winequality.red.csv', delimiter=';', skip_header=1)
#genfromtxt('filename', dtype (optional), delimiter (optional, skip header) to load data
print(wines)
print(wines[:, 0]) #first column only
print(wines[:, 0:1]).mean()    #first column & preserve the form

#Another example
grad_admission = np.genfromtxt('datasets/Admission_Predict.csv', dtype=None, delimiter=',', skip_header=1, names=('Serial No', 'GRE', 'IELTS', 'Uni Ranking', 'CGPA', 'Research', 'Chance'))
print(grad_admission.shape) #get dimension
grad_admission['CGPA'][0:5] #first 5 values of CGPA column

Res_exp = grad_admission[grad_admission['Research'] == 1]
#Boolean indexing to pull those with research exp
len(Res)    #No. of those students

print(grad_admission[grad_admission['Chance'] > 0.8]['GRE'].mean())
#Pull those with 80% chance and get their mean GRE score
print("")


#Regex
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

sum = 0
for i in range(11):
    sum = sum + i
    i = i + 1
print(sum, end= " ")
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum, end= " ")

import pandas as pd



