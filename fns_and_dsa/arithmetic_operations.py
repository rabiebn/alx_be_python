#!/usr/bin/python3

## Arithmetic Operations Function

def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                return "You can't divide by ZERO!"
            elif num2 != 0:
                result = num1 / num2
        case _:
            return
    return result