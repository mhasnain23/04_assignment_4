import random

def get_user_guess():
    """Prompt the user for a guess and validate it."""
    while True:
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        if guess in ['higher', 'lower']:
            return guess
        print("Invalid input. Please type 'higher' or 'lower'.")

def play_round(round_number, score):
    """Play a single round of the game."""
    print(f"\nRound {round_number}")
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    print(f"Your number is {user_number}")
    
    guess = get_user_guess()

    is_correct = (
        (guess == 'higher' and user_number > computer_number) or
        (guess == 'lower' and user_number < computer_number)
    )

    if is_correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print(f"Your score is now {score}")
    return score

def play_game():
    """Main function to play 5 rounds of the High-Low game."""
    print("Welcome to the High-Low Game!")
    print("-" * 32)
    
    score = 0
    total_rounds = 5
    
    for round_number in range(1, total_rounds + 1):
        score = play_round(round_number, score)
    
    print("\nThanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
