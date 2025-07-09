#!/bin/python3

# Personal Finance Calculator

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

projected = monthly_savings * 12 + monthly_savings * 12 * 0.05

print("Your monthly savings are $", monthly_savings, ".", sep="")
print("Projected savings after one year, with interest, is: $", int(projected), ".", sep="")
