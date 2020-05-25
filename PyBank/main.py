# imprt csv file
import csv
import os

# csv path

csvpath = os.path.join('Resources','budget_data.csv')

# Variables decreaselaration 

total_no_months = 0
total_profit_losses =0
month_change =[]
date_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0


# read csv file

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

# The total number of months and total amount of profit/losses
    previous_profit = int(row[1])
    total_no_months = total_no_months + 1
    total_profit_losses = total_profit_losses + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:
 
        total_no_months = total_no_months + 1
        total_profit_losses = total_profit_losses + int(row[1])

        #Change in profit/losses 
        change = int(row[1]) - previous_profit
        month_change.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
        #The greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        #The greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
      
    
    average_change = sum(month_change)/len(month_change)

    
    # Print the analysis to the terminal
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: " + str(total_no_months))
    print("Total: " + "$" + str(total_profit_losses))
    print("Average Change: "+ "$"  + str(average_change))
    print("Greatest increase in Profits: " + greatest_increase_month + " $"+ str(max(month_change)))
    print("Greatest decrease in Profits: " + greatest_decrease_month + " $"+  str(min(month_change)))

    # export the analysis to text file
    PyBank = open("analysis/PyBank_analysis.txt","w")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' + "Total Months: " + str(total_no_months)) 
    PyBank.write('\n' + "Total: " + "$" + str(total_profit_losses)) 
    PyBank.write('\n' + "Average Change: "+ "$"  + str(average_change)) 
    PyBank.write('\n' + "Greatest increase in Profits: " + greatest_increase_month + " $"+ str(max(month_change))) 
    PyBank.write('\n' + "Greatest decrease in Profits: " + greatest_decrease_month + " $"+  str(min(month_change))) 
