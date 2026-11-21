# Iterables = An object/collection that can returns its elements one at a time allowing it to be iterated over in a loop

# Array iterables
numbers = [1, 2, 3, 4]

for number in reversed(numbers):  # it'll print the numbers backward
    print(number, end=" ") # 4 3 2 1

# Set iterables
fruits = {"apple", "orange", "coconut"}

for fruit in fruits:
    print(fruit)
# String iterables
name = "testing a name"

for person in name:
    print(person)

# Dictionary

my_dictionary = {"A": 1, "B": 2, "C": 3}

for value in my_dictionary.values(): # values() will return values, keys() will return keys, items() will return both
    print(value)





