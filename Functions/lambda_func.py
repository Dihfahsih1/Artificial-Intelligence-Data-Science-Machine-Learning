add = lambda x,y: x+y
print(add(5,6))

square=lambda x: x**2
print(square(4))

nums = list(range(1,20,2))
square=list(map(lambda x: x**2, nums))
print(square)