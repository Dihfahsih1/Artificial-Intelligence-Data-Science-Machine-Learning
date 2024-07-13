class MyClass:
    def __init__(self, name):
        # self param is instance calling the method, it is the first param of the instance method
        self.Name=name
        
    def bark(self):
        return f"Hello, {self.Name}"
dog_input=input("Enter Dog Name: ") 
dog=MyClass(dog_input)

print(dog.bark())

    