
def calculator():
    print("Simple Calculator!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the number of the operation: ")
    
    if operation == '1':
        result = num1 + num2
        operation_name = "addition"
    elif operation == '2':
        result = num1 - num2
        operation_name = "subtraction"
    elif operation == '3':
        result = num1 * num2
        operation_name = "multiplication"
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_name = "division"
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice.")
        return
    
    print(f"\nThe result of the {operation_name} is: {result}")

if __name__ == "__main__":
    calculator()
