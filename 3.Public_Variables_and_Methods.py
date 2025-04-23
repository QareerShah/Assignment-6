class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand

    # Public method
    def start(self):
        print(f"{self.brand} car is starting...")

# Instantiate the class (object bana rahe hain)
my_car = Car("Toyota")

# Accessing public variable
print("Brand of the car:", my_car.brand)

# Calling public method
my_car.start()
