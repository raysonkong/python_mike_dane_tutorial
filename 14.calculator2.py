# 2:00:43
# Better Calculator  and using None

num1 = float(input("Enter first num: "))
op = input("Enter operator: ")
num2 = float(input("Enter second num: "))

result = None
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == '/':
    result = num1 / num2
else:
    result = "Not valid inputs!"


print(f"The result is: {result}")

