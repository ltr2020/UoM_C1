#NumPy
import numpy as np
a = np.array([[1,2.5,3], [4,5.8,6], [7,8,9]]) #float / int
print(a)
print(a[:,(0,2)])
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

#Try NumPy with Dataset
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