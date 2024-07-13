class Shape:
    def __init__(self, color,name,category):
        self.color=color
        self.name=name
        self.category=category
        
class Rectangle(Shape):
    def __init__(self,name,category, color, width, height):
        super().__init__(color,name,category) # call to the parent class constructor
        self.width=width
        self.height=height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
color=input("Enter The color: ")
height=int(input("Enter the height: "))
width=int(input("Enter the width: "))

rectangle=Rectangle(color,height, width)
print(f"The color of the Shape is: {rectangle.color} ")
print(f"The area of the rectangle is: {rectangle.area()}")
print(f"The Perimeter of the rectangle is: {rectangle.perimeter()}")

