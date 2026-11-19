import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

dice_dice = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}   

user_input = ""
saved_score = 0
while not user_input.lower() == 'q':
    score = 0
    quantity = input("How many dice would you like to roll? ")
    user_input = input("Press enter to roll the dice or 'q' to quit: ")
    for i in range(int(quantity)):
        dice = random.randint(1,6)
        score += dice
        for line in dice_dice[dice]:
            print(line)
    print(f"Your total score is: {score}, Would you like to save your score? (y/n) (it'll add to your saved score to your total score)")
    save_score = input()
    if save_score.lower() == 'y':
        saved_score += score
        print(f"Your saved score is: {saved_score}")
    else:
        print("Score not saved.")

print("Thanks for playing!")


        
