# class definition
class MyClass:
    pass

# Instance(object) creation
'''We create an instance of a class by calling it as if it were a function'''
obj=MyClass()

# __init__ ( Initialization Method )Attribute initialization

class MyClass1:
    def __init__(self, first_name, second_name, age):
        self.fname =first_name
        self.lname =second_name
        self.Age =age
    def print_age(self):
        return self.Age
    def full_name(self):
        return f"{self.fname} {self.lname}"

fn=input("Enter first Name: ")
ln=input("Enter Last Name: ")  
a=int(input("Enter Age: ")) 

#object creation(instantiation)     
firstclass = MyClass1(fn, ln,a)
secondclass= MyClass1("Mary","Jane",20)


print(firstclass.print_age())
secondclass.full_name()
    
        
    
    

      

