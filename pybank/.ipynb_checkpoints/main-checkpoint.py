from pathlib import Path
import csv
import numpy as np
​
csvpath = ('Resources/budget_data.csv')
=
#initialize variables
​
profits = []
#use csvreader to open file
with open (csvpath, 'r') as csvfile:
    
    #pass opened file into csv reader
    
    csvreader = csv.reader(csvfile, delimiter = ',')
​
#skip header and get profit values into profits list
    header = next(csvreader)
    
    for row in csvreader:
        
        profit = int(row[1])
        
        profits.append(profit)
            
# initialize metric variables then loop by rows
​
min_profit = 0
max_profit = 0
total_profit = 0
months_count = 0
min_profit_date = ""
average_delta_profit = np.mean(np.diff(profits))
​
for profit in profits:
​
    months_count += 1
​
    total_profit += profit
​
    if min_profit == 0:
        min_profit = profit
        max_profit = profit
    elif profit < min_profit:
        min_profit = profit

    elif profit > max_profit:
        max_profit = profit
        
#Output to text file
print("Financial Analysis")               
print("-------------------")
metrics = []
print(f"Total Months: {months_count}")
print(f"Total Profit: ${total_profit}")
print(f"Average Change: ${int(average_delta_profit)}")
print(f"Greatest Increase in Profits: ${max_profit}")
print(f"Greatest Decrease in Profits: {min_profit_date} ${min_profit}")
Financial Analysis
-------------------
Total Months: 86
Total Profit: $38382578
Average Change: $-2315
Greatest Increase in Profits: $1170593
Greatest Decrease in Profits:  $-1196225

