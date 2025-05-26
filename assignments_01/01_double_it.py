# double the user input


num = input("Enter a number to double it: ")


if num.isdigit():
    doubled = int(num) * 2
    print(f"The double of {num} is {doubled}.")
else:
    print("Please enter a valid number.")