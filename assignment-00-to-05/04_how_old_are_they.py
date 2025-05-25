# check that how old they are?

def main():
    alice: int = 18  # Alice's age is 18
    bob: int = alice + 2  # Bob is 2 years older than Alice
    clara: int = bob * 2  # Clara is twice as old as Bob
    david: int = clara - 5  # David is 5 years younger than Clara
    emma: int = alice + bob + clara + david  # Emma's age is the total of everyone else's

    # Print out all the ages!
    print("Alice is " + str(alice))
    print("Bob is " + str(bob))
    print("Clara is " + str(clara))
    print("David is " + str(david))
    print("Emma is " + str(emma))

main()
