#!/usr/bin/env python3

# Function convert_temp converts Celsius degrees to Fahrenheit degrees and vice versa.
# Enter degrees and select unit:
# 'f' - converts to Fahrenheit
# 'c' - converts to Celsius

def convert_temp(degrees, unit):
    if unit == 'f':
        res = degrees * 1.8 + 32
        print(f"{degrees}\N{DEGREE SIGN}C = {round(res)}\N{DEGREE SIGN}F")
    elif unit == 'c':
        res = (degrees - 32) * 0.5556
        print(f"{degrees}\N{DEGREE SIGN}F = {round(res)}\N{DEGREE SIGN}C")
    else:
        print("Incorrect unit. Please choose 'f' or 'c'.")


print("Example")
convert_temp(32, 'c')
convert_temp(0, 'f')
