import numpy as np

values = np.array([2,4,6,8,10])
sq = np.sqrt(values)
ex = np.exp(values)
logs = np.log(values)
sums = np.sum(values)
csum = np.cumsum(values)

print("The square root of your array is:",sq)
print("The exponential value of each is:",ex)
print("The log value of all element is:",logs)
print("The sum of all element is:",sums)
print("The cumulative sum is:",csum)