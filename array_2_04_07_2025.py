import numpy as np
print(np.random.rand(2))
print(np.random.rand(2,2))
print(np.random.randint(2))#prints random values upto 2 but not 2
print(np.random.randint(2,10))#from to 2 upto 10 but not 10
print(np.random.randint(2,10,3))#from 2 to 10 and generates set of 3 random values
print(np.random.randint(10,40,(10,10)))
mylist = [0,1,2,3,4,5]
arr = np.array(mylist)
print(arr.reshape(2,3))
print(arr)
b=np.random.randint(10,20,(5,4))
print(b)
print(b[:])
print(b[1:4])
