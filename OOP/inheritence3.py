# Multiple Inheritence
class LivingBeing:
    def __init__(self, name):
        self.name=name
        
#intermediate class
class Animal(LivingBeing):
    def __init__(self, name, species):
        super().__init__(name)
        self.species=species
        
#Derived Class
class Dog(Animal):
    def __init__(self,name, species, breed):
        super().__init__(name,species)
        self.breed=breed
        
    def details(self):
        return f"Name: {self.name}, Species: {self.species}, Breed: {self.breed}"

#creating an instance of a Dog
dog=Dog("Buddy", "Canine", "Germany Shepherd")
print(dog.details()) # call to a method from a derived class