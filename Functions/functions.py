# function definition
class func1():
    data = 1,2,3,4
    new_data=list(data)
    new_data.append(5)
    data=tuple(new_data)
    print(data)
    greeting=4
    print(type(data))

func1()
print(type(func1))



