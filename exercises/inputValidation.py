
is_invalid = True
while is_invalid:
    userInput = input("Please enter your username: ")
    if userInput.isalpha() and len(userInput) <= 12 and userInput.find(" ") == -1:
                print("Valid username.")
                is_invalid = False
    else:
        print("Invalid username. Please enter a valid username that is less than or equal to 12 characters, contains only letters, and does not contain any spaces or digits.")
