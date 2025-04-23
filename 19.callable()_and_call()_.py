class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the factor

    def __call__(self, number):
        # Multiply input number by the factor
        return number * self.factor


# Testing the Multiplier class
multiplier_by_2 = Multiplier(2)  # Create an instance with factor 2

# Checking if the object is callable
print(callable(multiplier_by_2))  # Output: True

# Using the object like a function to multiply
result = multiplier_by_2(5)  # This is equivalent to calling multiplier_by_2.__call__(5)
print(result)  # Output: 10 (5 * 2)
