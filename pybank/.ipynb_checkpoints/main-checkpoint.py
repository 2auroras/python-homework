#PYBANK Overview: Created 3 lists: months, profit, diff_profits.  Found min, max and averages with for loops and #conditionals. Used the index of the min_delta and max_delta lists to cross reference months list to pull the months. Had #to add one to index to compensate for index offset.  

from pathlib import Path
import csv


csvpath = ('Resources/budget_data.csv')

#initialize lists 
months  = []
profits = []
diff_profits = []

#use csvreader to open file
with open (csvpath, 'r') as csvfile:
    
    #pass opened file into csv reader
    
    csvreader = csv.reader(csvfile, delimiter = ',')

#skip header and get profit values into profits list and months into months list

    header = next(csvreader)
    
#populate lists - first months and profits with file open, then diff_profits with file closed

    for row in csvreader:
        month = (row[0])
        profit = int(row[1])
        months.append(month)
        profits.append(profit)
                  
#populate diff_profits list  

for i in range(len(profits) - 1):
    diff = (profits[i+1] - profits[i])
    diff_profits.append(diff)
            
            
# initialize metric variables 
min_profit = 0
max_profit = 0
max_delta = 0
min_delta = 0
total_delta = 0
total_profit = 0
months_count = 0


    
#Loop through diff_profits to find max_delta and min_delta
for delta in diff_profits:
    
    total_delta += delta
    
    if min_delta == 0:
        min_delta = delta
        max_delta = delta
    elif delta < min_delta:
        min_delta = delta
    elif delta > max_delta:
        max_delta = delta
        
#Loop through profits to find highest and lowest and total_month count and total profit 
for profit in profits:

    months_count += 1

    total_profit += profit
        
    if min_profit == 0:
        min_profit = profit
        max_profit = profit

    elif profit < min_profit:
        min_profit = profit

    elif profit > max_profit:
        max_profit = profit

# Find index for max_delta and min_delta so we can pass them into the months list to find corresponding month
# Note that the index must be increased by 1 because we are looking at the difference in two indexes 

index_max = (diff_profits.index(max_delta))+1
index_min = (diff_profits.index(min_delta))+1

#Print to terminal 

print("Financial Analysis")               
print("-------------------")
print(f"Total Months: {months_count}")
print(f"Total Profit: ${total_profit}")
print(f"Average Change: ${int(total_delta/months_count)}")
print(f"Greatest Increase in Profits:{months[index_max]}: ${max_delta}")
print(f"Greatest Decrease in Profits:{months[index_min]}: ${min_delta}")

# Save to txt file 
output_path = Path("Resources/pybank_output.txt")

with open(output_path, 'w') as file:
    file.write(f"Financial Analysis\n")               
    file.write(f"-------------------\n")
    file.write(f"Total Months: {months_count}\n")
    file.write(f"Total Profit: ${total_profit}\n")
    file.write(f"Average Change: ${int(total_delta/months_count)}\n")
    file.write(f"Greatest Increase in Profits:{months[index_max]}: ${max_delta}\n")
    file.write(f"Greatest Decrease in Profits:{months[index_min]}: ${min_delta}\n")
    
file.close()

