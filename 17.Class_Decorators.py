# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Adding greet method to the class
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Creating an object of Person class
person = Person("Alice")

# Calling the greet method
print(person.greet())  # Output: Hello from Decorator!
