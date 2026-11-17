
# Module 1: Length of a string. Length is a function in Python that returns the number of characters in a string. It includes spaces, punctuation, and special characters.
name = input("Enter your name: (ex: name)")

print(len(name)) # This will print the length of the string entered by the user.

# Module 2: Find Method. it's a string method that returns the index of the first occurrence of a substring in a string.

name.find("a") # This will return the index of the first occurrence of "a" in the string. If not found, it returns -1.

print(name.find("a")) # 1

name.rfind("a") # This will return the index of the last occurrence of "a" in the string. If not found, it returns -1.

print(name.rfind("a")) # 1

# Module 3: Capitalize Method. The capitalize() method returns a copy of the string with its first character capitalized and the rest lowercased.
name.capitalize() # This will return a copy of the string with its first character capitalized and

# Module 4: Upper Method. The upper() method returns a copy of the string with all the characters in uppercase.
name.upper() # This will return a copy of the string with all the characters in uppercase.

# Module 5: Lower Method. The lower() method returns a copy of the string with all the characters in lowercase.
name.lower() # This will return a copy of the string with all the characters in lowercase.

# Module 6: isdigit Method. The isdigit() method returns True if all the characters in the string are digits, otherwise it returns False.
name.isdigit() # This will return True if all the characters in the string are digits, otherwise it returns False.

# Module 7: isalpha Method. The isalpha() method returns True if all the characters in the string are alphabetic, otherwise it returns False.
name.isalpha() # This will return True if all the characters in the string are alphabetic, otherwise it returns False.

#  Module 8: count Method. The count() method returns the number of occurrences of a substring in the string.
name.count("a") # This will return the number of occurrences of "a" in the string.

# IMPORTANT!!!!
# Module 9: replace Method. The replace() method returns a copy of the string with all occurrences of a substring replaced with another substring.
newName = name.replace("a", "b") # This will return a copy of the string with all occurrences of "a" replaced with "b".

print(newName) # nbme


# Module 10: help(str) Method. The help() method is used to display the documentation of a string method.
print(help(str)) # This will display the documentation of a string method.