from operations import addition, subtraction, multiplication, division
print("Calculator Operations:")
while True:
    operations = input("Enter the operation (add(+), subtract(-), multiply(*), divide(/)): ").strip().lower()
    if operations == "exit":
        break
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    if operations == "add" or operations == "+":
        result = addition(x, y)
    elif operations == "subtract" or operations == "-":
        result = subtraction(x, y)
    elif operations == "multiply" or operations == "*":
        result = multiplication(x, y)
    elif operations == "divide" or operations == "/":
        result = division(x, y)
    else:        
        print("Invalid operation. Please try again.")
        continue
    print(f"The result of {operations} is: {result}")
