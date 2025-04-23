class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")


student = Student("Asad" , 26)
student.display()