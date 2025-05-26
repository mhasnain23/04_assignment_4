# ---------- Problem #1: List Practice ----------
def list_practice():
    # 1. Create a list of fruits
    fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]

    # 2. Print the length of the list
    print("Number of fruits:", len(fruit_list))

    # 3. Add 'mango' at the end
    fruit_list.append("mango")

    # 4. Print the updated list
    print("Updated fruit list:", fruit_list)


# ---------- Problem #2: Index Game Functions ----------


# Accessing elements safely
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range."


# Modifying elements safely
def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return "Element updated successfully."
    except IndexError:
        return "Error: Index out of range."


# Slicing the list safely
def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Error: Start or end index out of range."
    return lst[start:end]


# ---------- Game Interaction ----------
def index_game():
    game_list = [10, 20, 30, 40, 50]  # You can change this list
    print("\nWelcome to the Index Game!")
    print("Your starting list:", game_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            index = int(input("Enter the index to access: "))
            print("Result:", access_element(game_list, index))

        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(game_list, index, int(new_value)))
            print("Updated list:", game_list)

        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(game_list, start, end)
            print("Sliced list:", result)

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------- Main Function ----------
def main():
    print("== Problem 1: List Practice ==")
    list_practice()
    print("\n== Problem 2: Index Game ==")
    index_game()


# Run the program
if __name__ == "__main__":
    main()