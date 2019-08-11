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
        sales_items.append([item[4],item[3]])
        #sales_quantity.append(item[3])


## Report Dictionary
report={}


for menu_item in menu:
    quantity = int(0)
    for sale in sales_items:
        if menu_item[0] == sale[0]:
            quantity += int(sale[1])

    item_metrics = {'Price' :float(menu_item[1])},{'COGS' : float(menu_item[2])},{'Gross' : float(menu_item[1])-float(menu_item[2])},{'Number Sold' : quantity},{'Total Profit' : (quantity)*(float(menu_item[1])-float(menu_item[2]))} 

    key = menu_item[0]

    report[key] = item_metrics

for key,item_metrics in report.items():
    print(f"{key}\n{item_metrics}")





    
    




