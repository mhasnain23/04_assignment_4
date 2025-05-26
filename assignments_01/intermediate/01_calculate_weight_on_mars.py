# Constant for Mars gravity ratio
MARS_MULTIPLE = 0.378

# 1. Get the user's weight on Earth
earth_weight = input("Enter your weight on Earth (in kg): ")

# 2. Convert the input to a float
earth_weight = float(earth_weight)

# 3. Calculate the weight on Mars
mars_weight = earth_weight * MARS_MULTIPLE

# 4. Display the result
print(f"Your weight on Mars would be: {mars_weight:.2f} kg")
