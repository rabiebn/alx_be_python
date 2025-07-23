#!/usr/bin/python3

## Personal Daily Reminder

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if priority == "low":
    print("Note: ", end="")
else:
    print("Reminder: ", end="")
if time_bound == "no":
    print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
else:
    print(f"'{task}' is a {priority} priority task that requires immediate attention today!")


