class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass

# Create an object of D and call the show method
obj = D()
obj.show()  # This will show the MRO order
