
from operations import addition, subtraction, multiplication, division
print("Calculator Operations:")
def save_to_file(operation, x, y, result):
    with open("calculator_history.txt", "a") as file:
        file.write(f"{operation}: {x} and {y} = {result}\n")
while True:
    operations = input("Enter the operation (add(+), subtract(-), multiply(*), divide(/)): ").strip().lower()
    if operations == "exit":
        break
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    if operations == "add" or operations == "+":
        result = addition(x, y)
        save_to_file("Addition", x, y, result)
    elif operations == "subtract" or operations == "-":
        result = subtraction(x, y)
        save_to_file("Subtraction", x, y, result)
    elif operations == "multiply" or operations == "*":
        result = multiplication(x, y)
        save_to_file("Multiplication", x, y, result)
    elif operations == "divide" or operations == "/":
        result = division(x, y)
        save_to_file("Division", x, y, result)
    else:        
        print("Invalid operation. Please try again.")
        continue
    print(f"The result of {x} {operations} {y} is: {result}")
print("Calculator exited.")
