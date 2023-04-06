import csv

with open("/Resources/budget_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)

    total_months = 0
    net_total_amount = 0
    previous_amount = 0
    changes = []
    greatest_increase = 0
    greatest_decrease = 0

    for row in csv_reader:

        total_months += 1

        current_amount = int(row[1])
        net_total_amount += current_amount

        if previous_amount != 0:
            change = current_amount - previous_amount
            changes.append(change)

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        previous_amount = current_amount

    average_change = sum(changes) / len(changes)

    # Print the results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total Amount: ${net_total_amount}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

