def calc(starting_value):
    feet = starting_value // 12
    inches = starting_value % 12
    if type(starting_value) is int:
        return int(feet), int(inches)
    else:
        return float(feet), round(inches, 2)

input_value = input("Enter a number of inches: ")

try:
    int(input_value)
except ValueError:
    try:
        float(input_value)
    except ValueError:
        print("Please give a numeric input")
    else:
        feet, inches = calc(float(input_value))
        print(f"{int(feet)}' {inches}\"")
else:
    feet, inches = calc(int(input_value))
    print(f"{int(feet)}' {inches}\"")


