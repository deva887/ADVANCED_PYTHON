import numpy as np
my_list=[1,2,3,4,5]
arr=np.array(my_list)
print(my_list)
print(arr)
print(type(my_list))
print(type(arr))
print(np.arange(10))#upto 10
print(np.arange(10,20))#upto 20 from 10 
print(np.arange(10,50,5))#upto 50 from 10 with step 5
print(np.zeros(2,dtype=int))#1D array with zeros
print(np.ones(2,dtype=int))#1D array with ones
print(np.ones((2,2),dtype=int))#2d array with 2 rows and 2 columns with ones
print(np.zeros((3,3),dtype=int))#3D array with 3 rows and 3 columns with zeros