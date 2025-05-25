# Day 26 - A Simple Logger.
# topic - Decorators. 

# This function defines a simple logger decorator. Which takes another function as it's argument.
def simple_logger(func):
    # This function takes any no.of positionl and keyword args by *args and **kwargs respectively. 
    def wrapper(*args, **kwargs):
        # This displays the function name with no.of positional args and kwargs
        print(f"🚀 Running '{func.__name__}' with args: {args} kwargs: {kwargs}")

        # The args and kwargs will be passed into func and then result will be returned
        result = func(*args, **kwargs)
        print(f"✅ Finished '{func.__name__}', returned: {result}")
        print("-" * 40)
        return result
    return wrapper

# Example functions to decorate
# Calls it with different functions to log a simple msg
@simple_logger
def greet(name):
    return f"Hello, {name}!"

@simple_logger
def add(a, b):
    return a + b

@simple_logger
def divide(x, y):
    if y == 0:
        return "Can't divide by zero!"
    return x / y

# main
def main():
    # Calls all different methods
    greet("Jashwanth")
    add(10, 5)
    divide(8, 2)
    divide(5, 0)

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
