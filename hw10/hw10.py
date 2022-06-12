#!/usr/bin/env python3

# Input prompt

entered_number = int(input('Enter natural number -> '))

# Step counter

step = 0

# First IF statement checks, if the entered data is natural. If yes, then complete all the steps from the
# Collatz conjecture. If not, then print a message of running the program again and entering a natural number.

if entered_number > 0:
    print(f"Checking Collatz conjecture for number {entered_number}")
    while entered_number > 1:
        if entered_number % 2 == 0:
            entered_number = int(entered_number / 2)
            step = step + 1
            print(entered_number)
        else:
            entered_number = entered_number * 3 + 1
            step = step + 1
            print(entered_number)
else:
    print('Your number is not natural. Please, run the program again and enter natural number.')

# Print the result.

print(f"Number of steps is {step}.")