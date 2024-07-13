class A:
    default_name="John"
    def __init__(self,name,age):
        self.name =name
        self.age = age
    
    def display_name(self):
        return self.name

class B(A):
    def __init__ (self,name,age,height):
        super().__init__(name,age)
        self.height = height
    def display_height(self):
        return self.height

name =input("Enter Your Name: ")
age = int(input("enter your age: "))
height = int(input("enter your height: "))

object = B(name,age,height)
# print(f"Name: {object.display_name()}, Height: {object.display_height()} ")       
from bs4 import BeautifulSoup
import requests
url = "http://example.com"
response = requests.get(url)
if response.status_code == 200:
    print(response.text,"ok")
else:
    print("failed to retrieve")
    
    
 
 
    







    