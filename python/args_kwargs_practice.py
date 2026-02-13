def multiply(*args):
    """Multiplies all given numbers."""
    result = 1
    for i in args:
        result *= i
    return result

print(f"Multiplication Result: {multiply(1, 2, 3, 4, 5)}")

def average(*args):
    """Calculates the average of given numbers."""
    return sum(args) / len(args)

print(f"Average Result: {average(10, 10, 22)}")

def greet(message, *args):
    """Greets multiple people with a single message."""
    result = message + " "
    for name in args:
        result += name + " "
    return result

print(greet("Hello", "Ahmet", "Mehmet", "Ayse"))

def display_user_info(**kwargs):
    """Prints keyword arguments as a dictionary."""
    print(f"User Data Dictionary: {kwargs}")

display_user_info(name="Ahmet", surname="Yilmaz", age=30)

def complex_function(required_param, *args, **kwargs):
    """A function using fixed, positional, and keyword arguments together."""
    print(f"Required Parameter: {required_param}")
    print("-" * 20)
    print("Positional Arguments (*args):")
    for arg in args:
        print(arg)
    print("-" * 20)
    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

complex_function("Required Value", 2, 4, 5, 6, 3, name="Ahmet", surname="Yilmaz", age=30)
