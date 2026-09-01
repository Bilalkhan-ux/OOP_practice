from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def calcArea(self):
        pass

class Circle(shape):
    def __init__(self, r):
        self.r = r

    def calcArea(self):
        __area =  3.14159 * (self.r *self.r)
        return __area

    def getArea(self):
        return self.calcArea()


class rectangle(shape):
    def __init__(self , l , w):
        self.length = l
        self.width = w

    def calcArea(self):
        __area =  (self.width * self.length)
        return __area

    def getArea(self):
        return self.calcArea()

circle = Circle(5)
rectangle = rectangle(10,2)

print("Area of circle: ", circle.getArea())
print("Area of rectangle: ", rectangle.getArea())
