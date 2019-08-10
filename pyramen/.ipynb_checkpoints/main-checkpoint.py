#PYRAMEN

from pathlib import Path
import csv


csvmenu = ('Resources/menu_data.csv')
csvsales = ('Resources/sales_data.csv')

#Initialize lists

menu = []
sales = []


## MENU
#use csvreader to open file
with open (csvmenu, 'r') as csv_menu_file:
    
    #pass opened file into csv reader
    
    csvmenureader = csv.reader(csv_menu_file, delimiter = ',')

#skip header / create menu list

    header = next(csv_menu_file)
    
    for row in csv_menu_file:
        menu.append(row)
        
## SALES

with open (csvsales, 'r') as csv_sales_file:
    
    #pass opened file into csv reader
    
    csvsalesreader = csv.reader(csv_sales_file, delimiter = ',')
    
    header = next(csv_sales_file)
    
    for item in csvsalesreader:
        sales.append(row)

print(sales)


