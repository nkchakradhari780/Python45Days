class Student: 
    def set_names(self, name): 
        self.name = name
    
    def get_name(self):
        return self.name
    
student1 = Student()
student1.set_names("Nitin")
print(student1.get_name())