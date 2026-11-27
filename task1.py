import numpy as np
array_1D = np.arange(1,11)
print(array_1D)
print(array_1D.shape)
print("Datatype is:",array_1D.dtype)
# print(array_1D.ndim) ## i want to only this is 1d or not


array_2D = np.arange(1,10).reshape(3,3)
print(array_2D)
print(array_2D.shape)
print("Datatype is:",array_2D.dtype)
# print(array_2D.ndim) ## i want to only this is 2d or not

num_arr = np.array([10,20,30,40,50])
print(num_arr)
print(num_arr.shape)
print("Datatype is:",num_arr.dtype)