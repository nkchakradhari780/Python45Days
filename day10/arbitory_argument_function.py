# arbitory arguments 
# args is treated as a tuple 
def addAllNumbers(*args): 
    sum = 0
    for i in args:
        sum += i
    return sum

output = addAllNumbers(1,3,3,4,4,23,23,53,2,23)
print("The sum of all arguments: ", output)


# arbitory keyvalue arguments
# arguments are treated as dictionary 

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is: ", y)

studentInfo(name="Nitin", age=22, city="Durg")
studentInfo(name="Kundan", age=24, city="Durg")