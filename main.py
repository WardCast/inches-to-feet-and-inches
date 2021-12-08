def calc(starting_value):
    feet = starting_value // 12
    inches = starting_value % 12
    if type(starting_value) is int:
        return int(feet), int(inches)
    else:
        return float(feet), round(inches, 2)


input_value = input("Enter a number of inches: ")
repeat = True

while repeat:
    try:
        int(input_value)
    except ValueError:
        try:
            float(input_value)
        except ValueError:
            input_value = input("Please give a numeric input: ")
        else:
            repeat = False
            feet, inches = calc(float(input_value))
            print(f"{int(feet)}' {inches}\"")
    else:
        repeat = False
        feet, inches = calc(int(input_value))
        print(f"{int(feet)}' {inches}\"")


