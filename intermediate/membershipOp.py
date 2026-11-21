# Membership Operators = used to teste whether a value or variable is found in a sequence (string, list, tuple, set or dictionary)
# 1. in
# 2. not in

word = "apple"

letter = input("guess a letter in the secret word: ")

if letter in word: # you also can use the reverse 'not in'
    print(letter)
else:
    print("Doesn't exist")


email = "Test@gmail.com"

if "@" in email and "." in email:
    print("valid")
else:
    print("not valid")