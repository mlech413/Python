#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os
import csv

# input file
budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')
# output file
financial_analysis_txt = os.path.join('.', 'analysis', 'financial_analysis.txt')

total_months = 0
total_profit_loss = 0
current_change = 0
total_change = 0
average_change = 0
prev_amount = 0
greatest_increase_in_profits_month = ''
greatest_increase_in_profits_amount = 0
greatest_decrease_in_profits_month = ''
greatest_decrease_in_profits_amount = 0
lines = []

# open and read the csv file
with open (budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # read header row and skip
    csv_header = next(csvfile)
    
    # for loop through the rest of the file
    for row in csvreader:
        
        # TOTAL MONTHS
        # increment the month counter
        total_months += 1
        
        # TOTAL PROFIT/LOSS
        # add current amount to the total
        total_profit_loss += int(row[1])
        
        # If statement to ignore the first month because there is no previous month to calculate against
        if int(total_months) > 1:
            
            # calc current change (this month's amount - last month's amt) for avg change, greatest increase, greatest decrease
            current_change = int(row[1]) - int(prev_amount)
            
            # AVERAGE CHANGE
            # Subtract the previous amount from the current amount and add to the total change (will use later to calc avg)
            total_change = int(total_change) + current_change
            
            # GREATEST PROFIT INCREASE
            # Check current change vs previously stored amount for a new greatest increase
            if int(current_change) > int(greatest_increase_in_profits_amount):
                greatest_increase_in_profits_month = row[0]
                greatest_increase_in_profits_amount = current_change
                
            # GREATEST PROFIT DECREASE   
            # Check current change vs previously stored amount for a new greatest decrease
            if int(current_change) < int(greatest_decrease_in_profits_amount):
                greatest_decrease_in_profits_month = row[0]
                greatest_decrease_in_profits_amount = current_change

        # set the previous amount to compare with, for when the next row is read
        prev_amount = int(row[1])

# AVERAGE CHANGE
# Loop is finished so calculate the average change by dividing total change by the total months
average_change = round(int(total_change) / (int(total_months) - 1), 2)

# Format for displaying
total_profit_loss = '$' + str(total_profit_loss)
greatest_increase_in_profits_amount = '($' + str(greatest_increase_in_profits_amount) + ')'
greatest_decrease_in_profits_amount = '($' + str(greatest_decrease_in_profits_amount) + ')'

# set up all of the formatted output variables
blank = ''
line1 = ('Financial Analysis')
line2 = '--------------------------'
line3 = f'Total Months: {total_months}'
line4 = f'Total: {total_profit_loss}'
line5 = f'Average Change: {average_change}'
line6 = f'Greatest Increase in Profits: {greatest_increase_in_profits_month} {greatest_increase_in_profits_amount}'
line7 = f'Greatest Decrease in Profits: {greatest_decrease_in_profits_month} {greatest_decrease_in_profits_amount}'
# put together the List of the lines of output
lines = [line1, blank, line2, blank, line3, blank, line4, blank, line5, blank, line6, blank, line7]

# open and write output txt file
with open(financial_analysis_txt, 'w') as txtfile:

    for line in lines:
        
        # write each line to the terminal
        print(line)
        
        #write each same line to the output txt file
        txtfile.write(line)
        #line break for txt file
        txtfile.write('\n')
        


# In[ ]:





# In[ ]:





# In[ ]:




