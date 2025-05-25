# Prompt the user for temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Display the result
print(f"The temperature in Celsius is {celsius:.2f}")
