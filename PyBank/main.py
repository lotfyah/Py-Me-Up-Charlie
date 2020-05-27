# Import Modules

import os
import csv

# Variables declaration
total_months = 0
net_total_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# csv Path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read csv File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)


    # The total number of months and total amount of profit/losses
    previous_profit = int(row[1])
    total_months += 1
    net_total_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    for row in csvreader:
        
        # Total Number Of Months 
        total_months += 1

        # Net Total Amount Of "Profit/Losses" 
        net_total_amount += int(row[1])

        # Change in profit/losses
        revenue_change = int(row[1]) - previous_profit
        monthly_change.append(revenue_change)
        previous_profit = int(row[1])
        month_count.append(row[0])
        
        # The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # The Average
    average_change = sum(monthly_change)/ len(monthly_change)
    
   
# Print the analysis to the terminal
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${max(monthly_change)})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${min(monthly_change)})")



#Export the analysis to text file
PyBank = open("analysis/output.txt","w+")
PyBank.write(f"Financial Analysis\n")
PyBank.write(f"---------------------------\n")
PyBank.write(f"Total Months: {total_months}\n")
PyBank.write(f"Total: ${net_total_amount}\n")
PyBank.write(f"Average Change: ${average_change}\n")
PyBank.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${max(monthly_change)})\n")
PyBank.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${min(monthly_change)})\n")