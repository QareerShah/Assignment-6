# Step 1: Create a custom exception class
class InvalidAgeError(Exception):
    pass

# Step 2: Create the function to check age
def check_age(age):
    if age < 18:
        # Raise the custom exception if age is less than 18
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print(f"Age {age} is valid.")

# Step 3: Handle the exception using try...except
try:
    # Test the function by passing an invalid age
    check_age(15)
except InvalidAgeError as e:
    # Handle the custom exception
    print(f"Error: {e}")

# You can also test it with a valid age
try:
    check_age(20)
except InvalidAgeError as e:
    print(f"Error: {e}")
