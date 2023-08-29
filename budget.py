import csv

budget_csv = "PyBank/Resources/budget_data.csv"

with open(budget_csv, encoding="UTF-8") as budget_file:
    csvreader = csv.reader(budget_file)
    header_row = next(csvreader)
    months_number = []
    profit_value = []
    monthly_profit_loss = 0
    for month in csvreader:
        month_column = month[0]
        profits_column = int(month[1])
        monthly_profit_loss += sum({int(month[1])})
        if month_column not in months_number:
            months_number.append(month_column)
        if profits_column not in profit_value:
            profit_value.append(profits_column)
        greatest_profit = max(profit_value)
        lowest_profit = min(profit_value)
        if profits_column == greatest_profit:
            greatest_profit_month = month[0]
        if profits_column == lowest_profit:
            lowest_profit_month = month[0]
    average = monthly_profit_loss / len(months_number)
    print("Financial Analysis")
    print("____________________")
    print(f"Total Months {len(months_number)}")
    print(f"Total: ${monthly_profit_loss}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {greatest_profit_month} ${greatest_profit}")
    print(f"Greatest Decrease in Profits: {lowest_profit_month} ${lowest_profit}")