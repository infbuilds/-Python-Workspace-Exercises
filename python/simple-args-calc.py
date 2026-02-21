def universal_calculator(operation, *args):
    """
    A professional calculation tool that processes an unlimited number of arguments using *args.
    Supported operations: add, subtract, multiply, divide
    """
    
    # Error handling: Check if any numbers are provided
    if not args:
        return "Error: No numbers provided!"

    # Case-insensitive operation handling
    operation = operation.lower()

    # ADDITION
    if operation in ["add", "addition", "sum"]:
        result = sum(args)
        symbol = "+"

    # MULTIPLICATION
    elif operation in ["multiply", "multiplication", "product"]:
        result = 1
        for num in args:
            result *= num
        symbol = "*"

    # SUBTRACTION
    elif operation in ["subtract", "subtraction", "minus"]:
        result = args[0]
        for num in args[1:]:
            result -= num
        symbol = "-"

    # DIVISION
    elif operation in ["divide", "division"]:
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "Error: Division by zero is not allowed!"
            result /= num
        symbol = "/"

    else:
        return f"Invalid Operation: '{operation}'. (Supported: add, subtract, multiply, divide)"

    # Returning a formatted string with details
    return f"Operation: {operation.upper()} | Data: {args} | Result: {result}"

Testing the Function
if __name__ == "__main__":
    print(universal_calculator("add", 10, 5, 2))        
    print(universal_calculator("subtract", 100, 20, 5)) 
    print(universal_calculator("multiply", 3, 3, 3))    
    print(universal_calculator("divide", 50, 2, 5))     
