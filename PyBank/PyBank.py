# This Python script will analyzes the records to calculate each of the following:
# - The total number of months included in the dataset.
# - The net total amount of Profit/Losses over the entire period.
# - The average of the changes in Profit/Losses over the entire period.
# - The greatest increase in profits (date and amount) over the entire period.
# - The greatest decrease in losses (date and amount) over the entire period.
# This Python script will analyzes the records to calculate each of the following:
# - The total number of months included in the dataset.
# - The net total amount of Profit/Losses over the entire period.
# - The average of the changes in Profit/Losses over the entire period.
# - The greatest increase in profits (date and amount) over the entire period.
# - The greatest decrease in losses (date and amount) over the entire period.
from pathlib import Path
from pathlib import Path
# Imports the CSV module
import csv
budget_csv = Path("budget_data.csv")
profit_loss_dates = []
profit_loss = []
profit_loss_sum = 0
min_pl = 0
max_pl = 0
with open(budget_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)
    for row in csv_reader:
        profit_loss.append(int(row[1]))
        profit_loss_sum += int(row[1])
        profit_loss_dates.append(row[0])
profit_loss_change = []
for i in range(1, len(profit_loss)):
    x = profit_loss[i] - profit_loss[i - 1]
    profit_loss_change.append(int(x))
average_change_profitloss = round(sum(profit_loss_change)/len(profit_loss_change), 2)
min_pl = 0
max_pl = 0
for prof_loss in profit_loss:
    if prof_loss > max_pl:
        max_pl = prof_loss
    elif prof_loss < min_pl:
        min_pl = prof_loss
min_pl_index = profit_loss.index(min_pl)
max_pl_index = profit_loss.index(max_pl)
min_pl_date = profit_loss_dates[min_pl_index]
max_pl_date = profit_loss_dates[max_pl_index]
# Prints the Financial Analysis to the screen
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Financial Analysis")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Months: {len(profit_loss_dates)}")
print(f"Total: {profit_loss_sum}")
print(f"Average Change: {average_change_profitloss}")
print(f"Greatest Increase in Profits: {max_pl} on {max_pl_date}")
print(f"Greatest Decrease in Profits: {min_pl} on {min_pl_date}")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Creates a Financial Analysis file in text format
with open('financial_analysis.txt', 'w') as text:
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    text.write("Financial Analysis"+ "\n")
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    text.write("Total Months: " + str(len(profit_loss_dates)) + "\n")
    text.write("Total Profits: " + "$" + str(profit_loss_sum) +"\n")
    text.write("Average Change: " + '$' + str(float(average_change_profitloss)) + "\n")
    text.write("Greatest Increase in Profits: " + str(max_pl_date) + " ($" + str(max_pl) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(min_pl_date) + " ($" + str(min_pl) + ")\n")
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")