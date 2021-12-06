import math

def round_decimal(starting_value, inches):
    rounded_down_value = math.floor(starting_value)
    decimal = starting_value - rounded_down_value
    rounded_inches = round(inches, len(decimal))
    return rounded_inches


def calc(starting_value):
    feet = starting_value // 12
    inches = starting_value % 12
    if inches is int:
        return feet, inches
    elif inches is float:
        inches = round_decimal(starting_value, inches)
        return feet, inches


input_value = input("Enter a number of inches: ")

try:
    int(input_value)
except ValueError:
    feet, inches = calc(float(input_value))
    print(f"{feet}' {inches}\"")
else:
    feet, inches = calc(int(input_value))
    print(f"{feet}' {inches}\"")
