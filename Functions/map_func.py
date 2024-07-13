# map(function, iterable,.....)
def square(x):
    return x*x

numbers=list(range(1,6))
squared_numbers=map(square,numbers)

squared_numbers_list=list(squared_numbers)
print(squared_numbers_list)

add=lambda x,y: x+y

number1=[1,2,3,4,3]
number2=[5,6,7,8]
print(list(map(add, number1,number2))) #more pythonic

added_numbers=map(add, number1,number2)
added_numbers_list=list(added_numbers)
print(added_numbers_list)




