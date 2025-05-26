import random

# Generate a random number between 0 and 99
secret_number = random.randint(0, 99)
print("I am thinking of a number between 0 and 99...")

# Keep asking the user until they guess correctly
while True:
    guess = int(input("Enter a guess: "))

    if guess > secret_number:
        print("Your guess is too high\n")
    elif guess < secret_number:
        print("Your guess is too low\n")
    else:
        print(f"Congrats! The number was: {secret_number}")
        break
