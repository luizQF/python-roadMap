# collection = singles "variable" used to store multiple values

# Lists: [] ordered, mutable, allows duplicate elements
# Set : {} unordered, mutable, does not allow duplicate elements
# Tuple: () ordered, immutable, allows duplicate elements

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits2 = {"apple", "banana", "cherry", "kiwi", "mango"}

fruits3 = ("apple", "banana", "cherry", "kiwi", "mango")

# The main difference between a list and a tuple is that lists are mutable (can be changed) while tuples are immutable (cannot be changed). This means that you can add, remove, or modify elements in a list, but you cannot do the same with a tuple.
dir(fruits)  # This will show you all the methods available for lists
help(fruits)  # This will show you the documentation for lists

fruits.append("orange")  # This will add "orange" to the end of the list
fruits.remove("banana")  # This will remove "banana" from the list
fruits.insert(1, "blueberry")  # This will insert "blueberry" at index 1
fruits.sort()  # This will sort the list in ascending order
fruits.index("kiwi")  # This will return the index of "kiwi" in the list

fruits2.add("orange")  # This will add "orange" to the set
fruits2.remove("banana")  # This will remove "banana" from the set
fruits2.update(["blueberry", "strawberry"])  # This will add "blueberry" and "strawberry" to the set
fruits2.pop()  # This will remove a random element from the set

fruits3.count("kiwi")  # This will return the number of times "kiwi" appears in the tuple
fruits3.index("kiwi")  # This will return the index of "kiwi" in the tuple
# Tuple are faster than lists because they are immutable and have a smaller memory footprint. They are also hashable, which means they can be used as keys in dictionaries and elements in sets.

# 2D collection

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])  # This will print the first element of the first row (1)
print(matrix[1][2])  # This will print the third element of the second row
# [row][column]