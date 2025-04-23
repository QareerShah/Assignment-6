class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# Calling the static method directly from the class
result = MathUtils.add(5, 7)
print("The sum is:", result)
