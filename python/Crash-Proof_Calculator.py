def calculator(a, b, operation):
    """
    Handling the math logic here.
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation, fam."

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Pick an operation (add, subtract, multiply, divide): ").strip().lower()

    result = calculator(num1, num2, op)
    print(f"Result: {result}")

except ValueError:
    print("Yo, enter a valid number. Don't break the code.")
except ZeroDivisionError:
    print("Basic math, dude: You can't divide by zero.")
except Exception as e:
    print(f"Something went sideways: {e}")
