class Rectangl: 
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def perimeter(self): 
        return 2*(self.height + self.width)


rect1 = Rectangl()

rect1.set_dimensions(4,3)

print("Area is: ",rect1.area())
print("Perimeter is: ", rect1.perimeter())