from operations import add, subtract, multiply, divide
print("Calculator Operations:")
while True:
    operations = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operations == "exit":
        break
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
    else:        
        print("Invalid operation. Please try again.")
        continue
    print(f"The result of {operations} is: {result}")
