class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age) # call the parent class constructor(initializer)
        self.course=course
        
    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Course:{self.course}"
    
#Creating an instance of a student class
student = Student("Alice", 30, "Software Engineering")
print(student.display()) # Method overriding