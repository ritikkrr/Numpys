import numpy as np


a = np.array([10,20,30,40])
b = np.array([1,2,3,4])
adds = a +b
sub = a -b
mult = a *b
div = a/b
power = a**2
print("The addition of a and b is:",adds)
print("The subtraction of a and b is:",sub)
print("The multiplication of a and b is:",mult)
print("The division of a and b is:",div)
print("The power 2 of array a is:",power)


## Extra 
num_add = np.add(a,b)
print(num_add)
num_sub = np.subtract(a,b)
print(num_sub)
