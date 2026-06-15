from operations import add, subtract, multiply, divide
print("Calculator Operations:")
operations = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
if operations == "add":
    result = add(x, y)
elif operations == "subtract":
    result = subtract(x, y)
elif operations == "multiply":
    result = multiply(x, y)
elif operations == "divide":
    result = divide(x, y)
print(f"The result of {operations} is: {result}")
