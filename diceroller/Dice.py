import random

def roll_dice(number_of_dice):
    total = 0

    print("\nRolling Dice...\n")

    for i in range(number_of_dice):
        roll = random.randint(1, 6)
        print(f"Dice {i + 1}: {roll}")
        total += roll

    print(f"\nTotal = {total}")

print("Welcome to Dice Roller Simulator")

while True:
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("How many dice do you want to roll? "))
        roll_dice(num)

    elif choice == "2":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice. Try again.")