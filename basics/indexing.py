# indexing == acessing elements of a sequence using their index 

credit_number = "1234 5678 9012 3456"
print(credit_number[0])  # Output: 1
print(credit_number[5])  # Output: 5
print(credit_number[10])  # Output: 9
print(credit_number[15])  # Output: 3
print(credit_number[0:4])  # Output: 1234 you can also write [:4] without 0
print(credit_number[-1])  # Output: 6
print(credit_number[-4:])  # Output: 3456 you can also write [-4:] without -1
print(credit_number[::-1])  # Output: 6543 2109 8765 4321 this will reverse the string