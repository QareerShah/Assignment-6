class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation: Department holds a reference to Employee

    def show_department_info(self):
        print(f"Department: {self.name}")
        self.employee.display_info()  # Accessing Employee's method through aggregation

# Creating an Employee object independently
employee1 = Employee("Alice", "Software Engineer")

# Creating a Department object and passing the Employee object to it
department1 = Department("IT", employee1)

# Displaying department info and employee details
department1.show_department_info()
