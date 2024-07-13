#Base Class, Super Class, Parent Class

class Animal:
    def speak(self):
        return "Animal Speaks"
    
#Derived, Child, Sub Class
class Dog(Animal):
    def bark(self):
        return "Dog barks"
    def speak(self):
        return "Dog Speaks"
    
class Cat(Animal):
    def meows(self):
        return "Cat Meows"
    def speak(self):
        return "Cat Speaks"
    
#creating instances of a Dog and a Cat
dog=Dog()
cat=Cat()

print(dog.speak()) #inherited method
print(dog.bark()) #own method

print(cat.speak())
print(cat.meows())