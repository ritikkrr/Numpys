import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])
means = np.mean(marks)
medians = np.median(marks)
vari = np.var(marks)
stds = np.std(marks)
mins = np.min(marks)
maxs = np.max(marks)
ranges = maxs - mins

print("The mean of marks is:",means)
print("The median of marks is:",medians)
print("The variance of marks is:",vari)
print("The Standard deviation of marks is:",stds)
print(f"The min value is:{mins} and max values is:{maxs}")
print("The range of array is:",ranges)