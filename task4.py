import numpy as np
data = np.array([[10,20,30],[40,50,60],[70,80,90]])
row_sum = np.sum(data,axis=1)
col_sum = np.sum(data,axis=0)
min_value = np.min(data)
max_value = np.max(data)
means = np.mean(data)

print(data) ## I print only for view in output to confirm the output is right or not
print("The sum of row wise array :",row_sum)
print("The sum of column wise array:",col_sum)
print("The minimum value of array :",min_value)
print("The maximum value of array: ",max_value)
print("The mean value of array is ",means)