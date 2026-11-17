price1 = 3.14159
price2 = -987.292
price3 = 12.53

print(f"Price 1 is {price1:10}") # 10 spaces
print(f"Price 2 is {price2:010}") # 10 spaces filled with 0
print(f"Price 3 is {price3:<10}") # 10 spaces left aligne
#you can also use the format method to format the string
print("Price 1 is {:10}".format(price1)) # 10 spaces
print(f"Price 1 is {price1:+,.2f}") # + sign, comma as a thousands separator, and 2 decimal places