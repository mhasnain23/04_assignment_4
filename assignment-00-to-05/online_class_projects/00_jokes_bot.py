# Jokes Bot

JOKE = "Why don't scientists trust atoms? Because they make up everything!"
SORRY = "Sorry, I only know jokes."


def main():

    user_input = input("What do you want?")

    if "joke" in user_input.strip().lower():
        print(JOKE)
    else:
        print(SORRY)


main()
