class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        # Getter: Return the price
        return self._price

    @price.setter
    def price(self, value):
        # Setter: Update the price if it's a valid value
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        # Deleter: Delete the price
        print("Deleting the price...")
        del self._price


# Example usage
product = Product(100)

# Accessing the price using getter
print(product.price) 

# Updating the price using setter
product.price = 200
print(product.price) 

# Trying to set a negative price
product.price = -50  

# Deleting the price using deleter
del product.price  
