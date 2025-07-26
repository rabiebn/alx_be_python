#!/usr/bin/python3

## Explore `datetime` Module
from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days)
    future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")
