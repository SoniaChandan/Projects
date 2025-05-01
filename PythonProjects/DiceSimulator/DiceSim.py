import random


def title():
    """Dice 
    Simulator"""


def roll_dice():
    return random.randint(1, 6)


while True:
    input("Press enter to roll the dice ... ")
    result = roll_dice()
    print(f"You rolled a {result} \U0001F3B2")
    again = input("Roll again? (Y/N): ").lower()
    if again != "y":
        print("Thanks for playing")
        break
