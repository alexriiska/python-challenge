# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

#import modules
import os
import csv
from statistics import mean

#import the csv path
csvpath = "PyBank/Resources/budget_data.csv"

#create empty lists for row count (total months), total profit/loss (Column "B"), and changes in monthly profit 
rowcount = []
pnl = []
pnl_change = []

# Open the CSV
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skipping the header row
    csv_header = next(csvreader)
    
    #create a for loop to iterate through each row
    for row in csv.reader(csvfile):
                
        #add the data to the lists that were previously created
        
        #append the rowcount (total months) list for each row
        rowcount.append(row[0])
        
        #append the pnl list for data in column "B" - typecast because the data are integers
        pnl.append(int(row[1]))
        
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes    
    
    #create a for loop through the pnl list to calculate the monthly change
    for data in range(len(pnl)-1):
        
        #calculate the difference between Month N and Month N-1; add the calculated values to the pnl_change list
        pnl_change.append(pnl[data+1]-pnl[data])
        
        #caluclate the average change
        avg_change = mean(pnl_change)
        
        
#calculate the highest and lowest pnl change from the pnl change list
max_change = max(pnl_change)
min_change = min(pnl_change)


#find the month of the highest and lowest pnl change from the rowcount list
max_row = pnl_change.index(max(pnl_change)) + 1
min_row = pnl_change.index(min(pnl_change)) + 1


#print statements

print('Financial Analysis')
print('----------------------------')

#print the length (# of items) of the rowcount list
print(f'Total number of months: {len(rowcount)}')

#print the sum of the pnl list
print(f'Total: ${sum(pnl)}')

#print the average of the pnl_change list and round to 2 decimal points
print(f'Average Change: $ {round(avg_change,2)}')

#print the month of the highest increase in pnl, followed by the pnl change value
#typecast the integer value to a string
print(f'Greateest Increase in Profits: {rowcount[max_row]} (${(str(max_change))})')

#print the month of the highgest decrease in pnl, followed by the pnl change value
#typecast the integer value to a string
print(f'Greatest Decrease in Profits: {rowcount[min_row]} (${(str(min_change))})')


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open("Financial Analysis.txt", mode = "w") as file:
    file.write('Financial Analysis')
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write((f'Total number of months: {len(rowcount)}'))
    file.write("\n")
    file.write(f'Total: ${sum(pnl)}')
    file.write("\n")
    file.write(f'Average Change: $ {round(avg_change,2)}')
    file.write("\n")
    file.write(f'Greateest Increase in Profits: {rowcount[max_row]} (${(str(max_change))})')
    file.write("\n")
    file.write(f'Greatest Decrease in Profits: {rowcount[min_row]} (${(str(min_change))})')
