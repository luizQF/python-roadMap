# Python calculator
operator = input("Enter an operator: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = 0
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1 / num2
elif operator == "*":
    result = num1 * num2

print(f"result: {result:.2f}")