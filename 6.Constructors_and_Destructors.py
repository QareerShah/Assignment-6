class Logger:
    def __init__(self):
        print("Logger object created!")

    def __del__(self):
        print("Logger object destroyed!")


# Creating an object
log = Logger()

