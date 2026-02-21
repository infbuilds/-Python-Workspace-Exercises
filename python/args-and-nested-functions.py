def math_ops_wizard(*args):
    """
    A utility function that demonstrates nested functions 
    by calculating sum and product of given numbers.
    """
    
    # Check if any arguments were provided to avoid errors
    if not args:
        return "No numbers provided!"

    def calculate_sum(numbers):
        return sum(numbers)

    def calculate_product(numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    # Using dictionary-style return for better data handling
    total_sum = calculate_sum(args)
    total_product = calculate_product(args)
    
    return f"Numbers: {args} | Sum: {total_sum} | Product: {total_product}"

# Testing the code
print(math_ops_wizard(1, 2, 3, 4, 5))
print(math_ops_wizard(10, 20))
