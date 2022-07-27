# This Python script will analyzes the records to calculate each of the following:
# - The total number of months included in the dataset.
# - The net total amount of Profit/Losses over the entire period.
# - The average of the changes in Profit/Losses over the entire period.
# - The greatest increase in profits (date and amount) over the entire period.
# - The greatest decrease in losses (date and amount) over the entire period.
# pathlib allows you to iterate over that directory's content
from pathlib import Path
# Imports the CSV module
import csv
# Set the path to the csv file
budget_csv = Path("budget_data.csv")
# create lists
profit_loss_dates = []
profit_loss = []
profit_loss_change = []
# Set variables
profit_loss_sum = 0
PnL = 0
min_profit_loss = 0
max_profit_loss = 0
with open(budget_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)
    for row in csv_reader:
        profit_loss.append(int(row[1]))
        profit_loss_sum += int(row[1])
        profit_loss_dates.append(row[0])
for i in range(1, len(profit_loss)):
    x = profit_loss[i] - profit_loss[i - 1]
    profit_loss_change.append(int(x))
# Calculate the average
average_change_profitloss = round(sum(profit_loss_change)/len(profit_loss_change), 2)
for PnL in profit_loss:
    if PnL > max_profit_loss:
        max_profit_loss = PnL
    elif PnL < min_profit_loss:
        min_profit_loss = PnL
min_profit_loss_index = profit_loss.index(min_profit_loss)
max_profit_loss_index = profit_loss.index(max_profit_loss)
min_profit_loss_date = profit_loss_dates[min_profit_loss_index]
max_profit_loss_date = profit_loss_dates[max_profit_loss_index]
# Prints the Financial Analysis data to the screen
# The command print('\033[1m' + 'Text' + '\033[0m') prints the text in BOLD
print(f'\033[1m' + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\033[0m')
print(f'\033[1m' + 'Financial Analysis' + '\033[0m')
print(f'\033[1m' + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\033[0m')
print(f"Total Months: {len(profit_loss_dates)}")
print(f"Total: {profit_loss_sum}")
print(f"Average Change: {average_change_profitloss}")
print(f"Greatest Increase in Profits: {max_profit_loss} on {max_profit_loss_date}")
print(f"Greatest Decrease in Profits: {min_profit_loss} on {min_profit_loss_date}")
print(f'\033[1m' + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\033[0m')
# Creates a Financial Analysis file in text format
with open('financial_analysis.txt', 'w') as text:
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text.write("\n""Financial Analysis")
    text.write("\n""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    text.write("\n""Total Months: " + str(len(profit_loss_dates)))
    text.write("\n""Total Profits: " + "$" + str(profit_loss_sum))
    text.write("\n""Average Change: " + '$' + str(float(average_change_profitloss)))
    text.write("\n""Greatest Increase in Profits: " + str(max_profit_loss_date) + " ($" + str(max_profit_loss) + ")")
    text.write("\n""Greatest Decrease in Profits: " + str(min_profit_loss_date) + " ($" + str(min_profit_loss) + ")")
    text.write("\n""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
