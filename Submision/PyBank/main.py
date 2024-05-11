
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # declare variables
    number_of_months = 0 
    sum_profit = 0
    previous_month_profit = 0
    change_profit= []
    month_changes = []
    #loop trough the data
    for row in csvreader:
        number_of_months +=1
        sum_profit = sum_profit + int(row[1])

        #calculate the change between months
        if number_of_months == 1:
            previous_month_profit = int(row[1])
        else:
            change= int(row[1]) - previous_month_profit
            change_profit.append(change)
            month_changes.append(row[0])
            previous_month_profit = int(row[1])

    #calculate average
    average_change = sum(change_profit) / len(change_profit)
    #Calculate max
    max_changes = max(change_profit)
    max_month_index = change_profit.index(max_changes)
    max_month_changes = month_changes[max_month_index]
    #calculate min
    min_changes = min(change_profit)
    min_month_index = change_profit.index(min_changes)
    min_month_changes = month_changes[min_month_index]

    #print statements

    print('Financial Analysis')
    print("-------------------------------")
    print(f"Total Months: {number_of_months}")
    print(f"Total: ${sum_profit}")
    print(f"Avarage Change: {round(average_change,3)}")
    print(f'Greatest Increase in Profits: {max_month_changes} (${max_changes})')
    print(f"Greatest Decrease in Profits: {min_month_changes} (${min_changes})")
