#Activity 2 read me file notes upload and push function

import os
import csv

#Create file to read csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header


    Date_column = []
    Profit_loss = []
   
    for row in csvreader:
        # print(row[0])
        Date_column.append(row[0])
        Profit_loss.append(row[1])
#The total number of months included in the dataset
print(f'total months:{len(Date_column)}')

#The net total amount of "Profit/Losses" over the entire period
print(f'total amount: {int(sum(Profit_loss))}')

#The average of the changes in "Profit/Losses" over the entire period
print(f'Average Change:{sum(Profit_loss)} / {len(Date_column)}')

#The greatest increase in profits (date and amount) over the entire period
print

#The greatest decrease in losses (date and amount) over the entire period




#The total number of months included in the dataset
# def budgetsummary(profit_lose):

#         totalmonths = int(profit_lose[1])
#     print(f"Total Months: {sum(int(totalmonths))}")

# #The net total amount of "Profit/Losses" over the entire period
#     nettotal = int(profit_lose[2])
#     print(f"Total: {sum(int(nettotal)}")

# #The average of the changes in "Profit/Losses" over the entire period
#     averagetotal = nettotal / (totalmonths -1)
#     print(f"Average Change: {int(averagetotal)}")

# #The greatest increase in profits (date and amount) over the entire period


# Display_Budget = input("Would you like to see the budget Report? ")

# for row in budgetCSV:
#     if (Display_Budget == "yes"):
#         print(budgetsummary)

# #The greatest increase in profits (date and amount) over the entire period
# #The greatest decrease in losses (date and amount) over the entire period
#     if csv_header[1] = csv_header[1] -1
#     csv_header[2] -csv_header[2]
#     print(max(nettotal))
#     print(min(nettotal))
 



