## After many hours I consulted with a classmate to get what is seen below.  
# I am still having trouble accessing values of a key in a nested dictionary

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
    
    #only appended items to be used
    for item in csvsalesreader:
        sales_items.append([item[4],item[3]])
        


## Report Dictionary
report={}

##Iterated menu and create metrics dictionary
for menu_item in menu:
    #set each items quantity to 0 - this needs to be inside loop so it is reset for each item
    quantity = int(0)
##Iterated sales csv and used += to add up sales per item by name
    for sale in sales_items:
        if menu_item[0] == sale[0]:
            quantity += int(sale[1])
##Took numbers from menu and combined with quantity total gotten above
    item_metrics = {'Price' :float(menu_item[1])},{'COGS' : float(menu_item[2])},{'Gross' : float(menu_item[1])-float(menu_item[2])},{'Number Sold' : quantity},{'Total Profit' : (quantity)*(float(menu_item[1])-float(menu_item[2]))} 

    key = menu_item[0]

    report[key] = item_metrics
##Created two lists of dictionaries, one for items with sales and another for items that did not sell.  Printed both

items_with_sales = []
items_no_sales = []
item_sold={}
not_sold={}


for key,value in report.items():
    if (value[3]["Number Sold"]) > 0:
        item_sold = key,value 
        items_with_sales.append(item_sold)
    else:
        not_sold = key,value
        items_no_sales.append(not_sold)

print(items_with_sales)
print()
print(items_no_sales)
    



    




