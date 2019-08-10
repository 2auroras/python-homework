from pathlib import Path
import csv


csvmenu = ('Resources/menu_data.csv')
csvsales = ('Resources/sales_data.csv')

#Initialize lists

menu = []
sales_items = []


## MENU
#use csvreader to open file
with open (csvmenu, 'r') as csv_menu_file:
    
    #pass opened file into csv reader
    
    csvmenureader = csv.reader(csv_menu_file, delimiter = ',')

#skip header / create menu list

    header = next(csv_menu_file)
    
    for row in csvmenureader:
        menu.append([row[0],row[3],row[4]])
        
## SALES

with open (csvsales, 'r') as csv_sales_file:
    
    #pass opened file into csv reader
    
    csvsalesreader = csv.reader(csv_sales_file, delimiter = ',')
    
    header = next(csv_sales_file)
    
    for item in csvsalesreader:
        sales_items.append([item[4],int(item[3])])
        #sales_quantity.append(item[3])


## Report Dictionary
report={}
quantity = int(0)

for item in menu:
    key = item[0]
    value = [float(item[1]),float(item[2]),float(item[1])-float(item[2]),quantity]
    report[key] = value

    for items in report:

        for item in sales_items[0:10]:
            if item[0] in report:
                for item in sales_items:
                    quantity += (item[1])
                    value.append(quantity)


print(report)






