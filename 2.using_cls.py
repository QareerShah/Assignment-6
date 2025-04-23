class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        # Each time an object is created, increase the count
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Class method to show how many objects have been created
        print(f"Total objects created: {cls.count}")


# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Call class method to display count
Counter.show_count()
