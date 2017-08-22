# ## Option 1: PyBank
# ![Revenue](Images/revenue-per-lead.jpg)
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# * The total number of months included in the dataset
# * The total amount of revenue gained over the entire period
# * The average change in revenue between months over the entire period
# * The greatest increase in revenue (date and amount) over the entire period
# * The greatest decrease in revenue (date and amount) over the entire period
# As an example, your analysis should look similar to the one below:
# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```
# Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv
import sys
csvpath = os.path.join('Resources', 'budget_data_1.csv')

# Output
sys.stdout = open ('Financial Analysis.txt', 'w')

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    total_months = 0
    total_revenue = 0
    maximum = 0
    maxvalue = 0
    minvalue = 0
    #  Each row is read as a row
    next(csvreader, None)
    for row in csvreader:
        total_revenue += int(row[1])
        if row[0] != ' ':
            months=1
            total_months += months
            value = int(row[1])
            maxvalue = max(maxvalue, value)
            minvalue = min(minvalue, value)
            if value == maxvalue:
                maxdate = row[0]
            if value == minvalue:
                mindate = row[0]
       
    print("Total Months: " + str(total_months))
    print("Total Revenue: $" + str(total_revenue))

    average_revenue = total_revenue / total_months

    print("Average Revenue Change: $" + str(int(average_revenue)))
    print("Greatest Increase in Revenue: " + str(maxdate) + " ($" + str(maxvalue) + ")")
    print("Greatest Decrease in Revenue: " + str(mindate) + " ($" + str(minvalue) + ")")

# text_file = open('output.txt', 'w')
# text_file.write('pybank.py')

print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(int(average_revenue)))
print("Greatest Increase in Revenue: " + str(maxdate) + " ($" + str(maxvalue) + ")")
print("Greatest Decrease in Revenue: " + str(mindate) + " ($" + str(minvalue) + ")")
