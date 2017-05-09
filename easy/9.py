#!/usr/bin/env python3

values = []
new_value = ''
print("Enter digits.  To stop, type 'exit'")

while True:
    new_value = input("Enter a digit: ")
    if len(new_value) != 1 and new_value != 'exit':
        print("Error: Only input 1 value at a time")
        continue
    if new_value == 'exit': break
    values.append(new_value)

print(sorted(values))

