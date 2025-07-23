#!/usr/bin/python3

## 

size = int(input("Enter the size of the pattern: "))
line = size
while size > 0:
    for i in range(line):
        print("*", end="")
    print("")
    size -= 1
