import os
import csv

total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)

    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

for row in csvreader:
     total_months += 1
     net_amount += int(row[1])

     revenue_change = int(row[1]) - previous_row
     monthly_change.append(revenue_change)
     previous_row = int(row[1])
     month_count.append(row[0])

     if int(row[1]) > greatest_increase:
         greatest_increase = int(row[1])
         greatest_increase_month = row[0]



    