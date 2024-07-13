

def grade(mark):
    match mark:
        case mark if (mark>=80):
            print("A")
            
        case mark if(mark>=75):
            print("B")
            
        case mark if(mark>=70):
            print("C")
            
        case mark if(mark>=60):
            print("D")
            
        case _:
            print("F")

m = int(input("Enter a mark: "))

grade(m)
