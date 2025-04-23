class Dog:
    def __init__(self, name, breed):
        self.name = name   # Instance variable for dog's name
        self.breed = breed # Instance variable for dog's breed

    def bark(self):
        print(f"{self.name} says woof!")

# Creating a Dog object
dog1 = Dog("Buddy", "Golden Retriever")

# Calling the bark method
dog1.bark()  # Output: Buddy says woof!
