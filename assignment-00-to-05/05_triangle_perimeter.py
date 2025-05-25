def calculate_triangle_perimeter():
    print("Let's calculate the perimeter of your triangle!")

    a = float(input("Enter the first side (a): "))
    b = float(input("Enter the second side (b): "))
    c = float(input("Enter the third side (c): "))

    perimeter = a + b + c
    print("🟢 The total perimeter is: " + str(perimeter) + " units")

# Call the function
calculate_triangle_perimeter()

# Output example:
# Let's calculate the perimeter of your triangle!
# Enter the first side (a): 3
# Enter the second side (b): 4
# Enter the third side (c): 5
# 🟢 The total perimeter is: 12.0 units