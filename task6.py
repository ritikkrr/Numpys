import numpy as np

marks = np.array([78,85,90,66,72,88,95,60])
sorts = np.sort(marks)

p25 = np.percentile(marks,25)
p50 = np.percentile(marks,50)   
p70 = np.percentile(marks,70)


avgs = np.mean(marks)
above_avg_count = np.sum(marks>avgs)


print("The sort value of marks is:",sorts)
print("The 25 percentile value is:",p25)
print("The 50 percentile value is:",p50)
print("The 70 percentile value is:",p70)
print("The above_avg_count is:",above_avg_count)