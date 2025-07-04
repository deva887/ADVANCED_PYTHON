import numpy as np
#creating arrays
narray=[0,1,2,3,4,5,6]
arr=np.array(narray)#np.array() creates an array from a list
print(type(arr))
print(arr)
#arange
print(np.arange(10))#upto 10 means 0 to 9
print(np.arange(10,20))#upto 20 from 10 means 10 to 19 Note:first arg< second arg
print(np.arange(10,50,5))#upto 50 from 10 means 10 to 49 with step 5
#zeros
print(np.zeros(7,dtype=int))#1D array
print(np.zeros((2,2),dtype=int))#2D array
print(np.zeros((5,6),dtype=int))#2D array with 5 rows and 6 columns
#using a variable
n=(4,4)
print(np.zeros(n,dtype=int))
#ones
print(np.ones(1,dtype=int))
print(np.ones(5,dtype=int))
print(np.ones((3,3),dtype=int))
print(np.ones((5,6),dtype=int))
#random and rand
print(np.random.randint(5))#np.random.randint is to print single random number upto 5 but not 5
print(np.random.randint(4,10))#np.random.randint is to print single random number from 4 to 9
print(np.random.randint(0,10,4))#prints the array of 4 numbers 
print(np.random.randint(5,9))
print(np.random.randint(10,40,(4,4)))
#reshape
print(np.arange(1,13).reshape(4,3))
print(np.arange(1,13).reshape(12,1))
print(np.arange(1,13).reshape(1,12))
print(np.arange(1,13).reshape(6,2))
#slicing
print(np.random.randint(10,20,(5,5)))
b=np.random.randint(10,20,(8,8))
print(b)
print(b[:])#prints entire array
print(b[1:3])#prints rows from 1 to 2
print(b[1,2])
print(b[5,4])
print(b[5,-3])
print(b[0:-2])
print(b[-6:6])
print(b[-1,-2])
c=np.random.randint(10,20,(8,8))
print(c)
print(c[4])
print(c[:,6])
#
d=np.arange(0,100).reshape(10,10)
print(d)
print(d[::-1])
print(d[::-2])
print(d)
print(d[4:6,4:6])
# filterting
print(d)
print(d[d>50])
print(d[d>=50])
print(d[d==50])