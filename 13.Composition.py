class Engine:
    def start(self):
        print("Engine is starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine object
    
    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Accessing Engine's method via Car

# Creating an Engine object
engine = Engine()

# Passing the Engine object to the Car class during initialization
car = Car(engine)

# Starting the car (which starts the engine as well)
car.start_car()
