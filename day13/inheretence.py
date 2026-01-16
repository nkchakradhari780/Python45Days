class Parent: 
    def __init__(self): 
        self.super_attribute = True
        print("This is the parent class")

class Child(Parent): 
    def __init__(self):
        super().__init__()
        print("this is a child class")


child = Child()
print(child.super_attribute)

