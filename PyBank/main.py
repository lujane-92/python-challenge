import os
import csv

bank_csv = os.path.join("/Users/lujan/Downloads/Instructions/PyBank/Resources/budget_data.csv")

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    dates = []
    months = []
    total_profit = 0
    total_monthly_change = 0

    for row in csvreader:
        date = row[0]
        dates.append(date)
        month = row[1]
        months.append(month)
        total_profit = total_profit + int(month)
    
    monthly_change = [int(months[i + 1]) - int(months[i]) for i in range(len(months)-1)] 

    max = 0
    min = 0

    for month in monthly_change:
        total_monthly_change = total_monthly_change + month
    
    average = float("{0:.2f}".format(total_monthly_change/len(monthly_change)))

    for month in monthly_change:
        if int(month) > max:
            max = int(month)       

    for month in monthly_change:
        if int(month) < min:
            min = int(month)

print ("Financial Analysis")
print ("----------------------------")
print (f"Total Months: {len(months)}")
print (f"Total: ${total_profit}")
print (f"Average Change: ${average}")
print (f"Greatest Increase in Profits: {dates[monthly_change.index(max)+1]} ${max}")
print (f"Greatest Decrease in Profits: {dates[monthly_change.index(min)+1]} ${min}")

output_file = os.path.join("/Users/lujan/Desktop/Financial_Analysis_Summary.txt")


with open(output_file,"w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${total_profit}")
    file.write("\n")
    file.write(f"Average Change: ${average}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {dates[monthly_change.index(max)+1]} ${max}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {dates[monthly_change.index(min)+1]} ${min}")