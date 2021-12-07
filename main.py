import math

def calc(starting_value):
    feet = starting_value // 12
    inches = starting_value % 12
    if type(starting_value) is int:
        return int(feet), int(inches)
    else:
        return float(feet), round(inches, 2) # If you don't need rounding remove round(...)

input_value = input("Enter a number of inches: ")

try:
    feet, inches = calc(float(input_value))
    print(f"{feet}' {inches}\"")
except ValueError:    
    print("Error: Something wrong with your input")
