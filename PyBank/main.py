# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
greatest_inc = ["", 0]
greatest_dec = ["", 999999999999999999]


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_value = int(first_row[1])
    

    # Track the total and net change
    

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        total_net += int(row[1])

        # Track the net change
        current_profit = int(row[1])

        net_change = current_profit - previous_value

        net_change_list.append(net_change)

        previous_value = current_profit

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_inc[1]:
            greatest_inc = [row[0], net_change]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_dec[1]:
            greatest_dec = [row[0], net_change]


# Calculate the average net change across the months
average_net_change = sum(net_change_list)/len(net_change_list)

# Generate the output summary


# Print the output
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_net_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})")
print(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_net_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n")
