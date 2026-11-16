item = input("Enter the item you want to add to the shopping cart: ")
price = float(input(f"Enter the price of {item}: ")) # remember to typecast the value to float since input() returns a string
quantity = int(input(f"Enter the quantity of {item}: ")) # same here >:(
total = price * quantity
print(f"The total cost of {quantity} {item}(s) is: ${total:.2f}") #.2f means to format the float to 2 decimal places