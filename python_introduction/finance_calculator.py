#!/bin/python3

# Personal Finance Calculator

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

savings = income - expenses

projected = savings * 12 * 1.05

print("Your monthly savings are $", savings, ".", sep="")
print("Projected savings after one year, with interest, is: $", projected, ".", sep="")
