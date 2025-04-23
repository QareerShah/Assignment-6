class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

# Teacher class inherits from Person
class Teacher(Person):
    def __init__(self, name, subject):
        # Using super() to call the base class constructor
        super().__init__(name)  # Calls Person's __init__
        self.subject = subject

    def display_subject(self):
        print(f"Subject: {self.subject}")

# Creating a Teacher object
teacher = Teacher("Mr Ali", "Mathematics")

# Calling methods from both classes
teacher.display_name()   # From Person
teacher.display_subject()  # From Teacher
