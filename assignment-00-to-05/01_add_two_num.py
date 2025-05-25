# add two numbers sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def add_two_numbers(a, b):
    """Function to add two numbers."""
    return a + b

result = add_two_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")
