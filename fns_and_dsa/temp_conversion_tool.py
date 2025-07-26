#!/usr/bin/python3

## Temperature Conversion Tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    temp = input("Enter the temperature to convert: ")
    try:
        temp = float(temp)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    match unit:
        case "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        case "F":
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
        case _:
            print("Invalid input.")


if __name__ == "__main__":
    main()