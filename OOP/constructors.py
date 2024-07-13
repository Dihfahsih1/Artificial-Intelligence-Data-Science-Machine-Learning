# Constructor is a special method that is called when an object is created
# Purpose of a constructor is used to initialize the object's attributes
# The name of this method is '__init__()'
# Name  : __init__()
# First Param: self
# Other Params, param1 .....param_no.

class Person:
    def __init__(self, age,name):
        self.age=age
        self.name=name
                
#creating an instance of class Person
obj=Person(20,"Alice") #this is a person class constructor
print(f"Name:{obj.name} - Age: {obj.age}")

# A constructor with default values
class Person1:
    def __init__(self, age=10,name="Mary"):
        self.age=age
        self.name=name
                
#creating an instance of class Person
obj=Person1(20,"Alice") #this is a person class constructor
print(f"Name:{obj.name} - Age: {obj.age}")

# A constructor with No Parameters
class Person2:
    params="Constructor has no params"
                
#creating an instance of class Person
obj1=Person2() #this is a person class constructor
print(obj1.params)

