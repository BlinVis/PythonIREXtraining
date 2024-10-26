from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,rrezja):
        self.rrezja=rrezja
    def area(self):
        return 3.14 * (self.rrezja**2)

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2

rrethi=Circle(5)
print(rrethi.area())


