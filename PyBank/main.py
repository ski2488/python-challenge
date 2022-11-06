#PyBank Challenge
#Load packages
import os
import csv

#Declare variables
months = 0
profit = 0
cum_profit = 0
months_list = []
change = []

#Import csv data
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #print(row)
        
        #Count months
        months = months + 1
        
        #Month-over-month profit change
        if cum_profit == 0:
            delta_profit = 0
            profit = int(row[1])
        else:
            delta_profit = int(row[1]) - profit 
            profit = int(row[1])
        
        #Cumulative profit
        cum_profit = cum_profit + int(row[1])

        #Build list of months
        months_list.append(row[0])
        #Build list of month-over-month profits
        change.append(delta_profit)

#Calculate non-iterated metrics
avg_change = round(sum(change) / (len(change) - 1), 2)
max_change = max(change)
min_change = min(change)
max_month = months_list[change.index(max_change)]
min_month = months_list[change.index(min_change)]

#Print results
results1 = f"Total Months: {months}"
results2 = f"Total: ${cum_profit}"
results3 = f"Average Change: ${avg_change}" 
results4 = f"Greatest Increase in Profits: {max_month} (${max_change})"
results5 = f"Greatest Decrease in Profits: {min_month} (${min_change})"
resultsfinal = [results1, results2, results3, results4, results5]

for item in resultsfinal:
    print(item)
    print('\n')

#Export to txt file
with open('analysis/results.txt', 'w') as f:
    for item in resultsfinal:
        f.write(item)
        f.write('\n')
