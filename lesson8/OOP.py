


class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width
    def calculate_perimeter(self):
        return 2*(self.length+self.width)

drejtkendeshi=Rectangle(2,5)

print(drejtkendeshi.calculate_perimeter())



