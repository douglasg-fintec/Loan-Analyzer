# coding: utf-8
import csv
from pathlib import Path

"""Automate the calculations for the loan portfolio summaries."""

# List of loan costs in the portfolio
loan_costs = [500, 600, 200, 1000, 450]


"""Get the profile of loan portfolio summaries."""

#Calculate the total number of loans in the portfolio.
total_number_of_loans = len(loan_costs)
# Print the number of loans in the portfolio
print(f"The total number of loans in the list: {total_number_of_loans}")


#Calculate the total of loan costs in the portfolio.
total_value_of_loans = sum(loan_costs)
# Print the sum of all loans from the list
print(f"The sum of all loans in the list: ${total_value_of_loans}")


# Define function the calculate the average of two numbers
def calculate_average(number_one, number_two):
    average = number_one/number_two
    return average

#Calculate the average loan amount
average_loan_amount = calculate_average(total_value_of_loans,total_number_of_loans)
# Print the average loan amount of all loans from the list
print(f"The average loan amount of loans in the list: ${average_loan_amount}")

"""
Analyze the loan to determine the investment evaluation.
Calculates a Present Value, or a "fair price" for what this loan would be worth using a minimum required return of 20% as the discount rate.
"""
# Calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Get the value of 'future_value'from the dictionary. Return 0 if the value is not there
future_value = loan.get("future_value",0)
# Print the value of future_value
print(f"The fair value of the loan: ${future_value}")

# Get the value of 'remaining_months'from the dictionary. Return 0 if the value is not there
remaining_months = loan.get("remaining_months",0)
# Print the value of remaining_months
print(f"The remaining months on the loan: {remaining_months} months")


# Calulate present value from the specified value od the parameters. If annual_discount_value/12  is passed  returns  monthly based "fair value"
# if annual_discount_value is used the annual based present value is retunred.

def calculate_present_value(future_value_parameter,remaining_months_parameter,discount_rate_parameter):
    present_value = future_value_parameter / (1 + discount_rate_parameter) ** remaining_months_parameter
    return present_value

# Define gloabl varaible for the discount
annual_discount_rate = .20

# Adjust the discount rate to force the use the use of the **monthly** version of the present value formula.
# fair_value_discount_rate = annual_discount_rate /12

fair_value = calculate_present_value(future_value,remaining_months, (annual_discount_rate /12))

# Determine if the present value represents the loan's fair value.
print (f"The fair value of the loan is: ${fair_value:.2f}")

# Check if presnet value represents the fair value
if fair_value >= loan["loan_price"]:
    # Present value of the loan is greater than or equal to the cost
    print(f"The loan fair value is worth at least the cost of the loan to buy it. ")
else:
    # Present value of the loan is less than or equal to the cost
    print("The loan is too expensive and not worth the price.")
    

"""Perform financial calculations using functions."""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
"""
# Call the previouly defined function for "calculate_present_value" passing in values from the remaining_months and future_value on the new_loan dictionary. 
# Using the # global value for the present value give us a calulation on an annual based discount_rate
"""

# Annual_discount_rate is 20% - defined above

# Calculate the present value of the new loan using calculate_present_value function defined above
present_value = calculate_present_value(new_loan.get("future_value"),new_loan.get("remaining_months"),annual_discount_rate)
print(f"The present value of the loan is: {present_value:.2f}")


""" Conditionally iterate through series of loans and select only the inexpensive loans."""

# A list of loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called that will contain the inexpensive loans cost < 500
inexpensive_loans = []

"""" Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list """

# loop through the list of loans
for loan in loans:
    #check each loan in the list and see if the loan price is less than or equal to $500
    #if so add that loan to the inexpensive loan list
    if loan["loan_price"] < 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print(f"The following loans have been added to the inexpensive loans list {inexpensive_loans}")


"""Output this list of inexpensive loans to a csv file"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Open a new CSV file.
#NOTE "closedfd=True to ensure the file is closed properly"
with open(output_path, 'w',newline = '', closefd=True) as csvfile:
     csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

     # write the header row
     csv_writer.writerow(header)
     # write the values in each row each row of loan.values()
     for loan in inexpensive_loans:
    # write the values from each loan to the csv file
        csv_writer.writerow (list(loan.values()))  