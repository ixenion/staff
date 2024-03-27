import numpy as np

a = np.arange(15).reshape(3, 5)#generate array 3x5 from 0 to 14
#print(a)

#attributes:
print(f"ndarray.ndim {a.ndim}")#return 2      #number of dimentions
print(f"ndarray.shape {a.shape}")#ret (3, 5)  #dimentions of the array
print(f"ndarray.size {a.size}")#ret 15        #total number of array's elements
print(f"ndarray.dtype {a.dtype}")#ret int64   #type of the elements of the array
print(f"ndarray.itemsize {a.itemsize}")#ret 8 #the size in bytes of each element of the array
print(f"ndarray.data {a.data}")               #the buffer containing the actual elements of the array

##array creating

a = np.array([2,3,4])#int  RIGHT
#a = np.array(2,3,4)       WRONG
b = np.array([1.2,3.5,5.1])#float
c = np.array([(1,2,3), (4,5,6)])#two dimention array
a = np.array([[1,2], [3,4,]], dtype=complex)#   (1.+j) and so on
b = np.zeros((3,4))#creates array of zeros
c = np.ones((3,4), dtype=np.int16)#ones. dtype is optional. by default dtype=float64
d = np.empty((2,3))#content of array depends on the state of the memory
print(d)

a = np.arange(10, 30, 5)#analog of range. 10 is first element, 5 is step, 30 is ceiling
print(np.arange(0, 2, 0.3))
b = np.linspace(0, 2, 9)# 9 numbers from 0 to 2

#return an array of zeros with the same shape and type as a given array (b)
c = np.zeros_like(b, dtype=None, order='K', subok=True, shape=None)
d = np.ones_like(b, dtype=None, order='K', subok=True, shape=None)
a = np.empty_like(b, dtype=None, order='K', subok=True, shape=None)
print(a)

#bidimentional array;
b = np.arange(12).reshape(4,3)
print(b)
#tridimentional array
c = np.arange(24).reshape(2,3,4)
print(c)

#if an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners
print("")
print(np.arange(10000))
#to disable this:  np.set_printoptions(threshold=np.nan)

############################################################################
##Basic operations

a = np.array([10, 20, 40, 30])
b = np.arange(4)
c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a>35)

print(a*b)#elementwise product
print(a @ b)#matrix product
print(a.dot(b))#also matrix prouct


