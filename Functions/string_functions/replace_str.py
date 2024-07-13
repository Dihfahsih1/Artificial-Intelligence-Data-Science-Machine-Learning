def replace_func(x, y, w):
    new_string=x.replace(y, w)
    return new_string
    
    
string =input("Enter The string")
old=input("Enter the word to be replaced")
new=input("Enter the word to replace with")
print(replace_func("Python Sucks", "Sucks","Enjoyable"))