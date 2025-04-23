class Employee:
    def __init__(self):
        self.name = "Ali"           # Public
        self._salary = 50000        # Protected
        self.__ssn = "123-45-6789"  # Private


# Create an object
emp = Employee()

# Accessing public variable
print("Public - Name:", emp.name)  # ✅ Accessible

# Accessing protected variable
print("Protected - Salary:", emp._salary)  # ⚠️ Accessible but not recommended

# Accessing private variable directly (will give error)
try:
    print("Private - SSN:", emp.__ssn)
except AttributeError:
    print("Private - SSN: ❌ Can't access directly")

# Accessing private variable using name mangling
print("Private - SSN (using name mangling):", emp._Employee__ssn)
