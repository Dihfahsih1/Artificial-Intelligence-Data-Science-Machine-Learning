def registration(name=None,age=None,course=None):
    # registration function
    
    '''The funtion for registering the name, age and course'''
    if name is None:
        name=input("Enter the name: ")
    
    if age is None:
        age=int(input("Enter the age: "))
        
    if course is None:
        course=input("Enter the course: ")
    user_info={"name":name, "age":age, "course":course}
    
    return user_info

def profile(data):
    return f"NAME: {data['name']},\nAGE: {data['age']},\nCOURSE: {data['course']}"

user_data=registration()
len(user_data)
print(profile(user_data))

