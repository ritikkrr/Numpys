import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])
weekly_sales = np.sum(sales)
average_sales = np.mean(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)
standard_deviation = np.std(sales)
above_average = np.where(sales > average_sales)
above_average_value = sales[sales > average_sales]


print("The total weekly sales is:",weekly_sales)
print("The average weekly sales is:",average_sales)
print("The maximum weekly sales is:",max_sales)
print("The minimum weekly sales is:",min_sales)
print("The standard deviation of weekly sales is:",standard_deviation)
print("The number of weeks with sales above the average is:",above_average) 
print("The weeks with sales above the average are:",above_average_value) 