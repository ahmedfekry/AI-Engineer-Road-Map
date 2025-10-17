try:
    number = float(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(f"Invalid Input, {err}")

