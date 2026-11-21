# list comprehension = a concise way to create lists in python compact and easier to read than traditional loops [expression for value in iterable if codition]
 
# without comprehension list
doubles = []

for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

# using comprehension list

# doubles = [expression for value in iterable if condition]

triples = [x * 3 for x in range(1,11)]

print(triples)

# Array

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# Condition

numbers = [1, 34, 54, 3, -12, -5]

pos_num = [num for num in numbers if num >= 0]
print(pos_num)