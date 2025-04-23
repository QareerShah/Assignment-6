# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Call the original function
    return wrapper

# Function to apply the decorator to
@log_function_call  # This applies the decorator
def say_hello():
    print("Hello!")

# Calling the function
say_hello()
