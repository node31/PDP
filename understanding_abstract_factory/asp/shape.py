import abc
from understanding_abstract_factory.asp.abstract_factory import AbstractFactory
class Shape(metaclass=abc.ABCMeta):
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print("Drawing %s" % self.__class__.__name__)

class Rectangle(Shape):
    def draw(self):
        print("Drawing %s" % self.__class__.__name__)

class ShapeFactory(AbstractFactory):
    def getColor(self, colorType):
        raise NotImplementedError

    def getShape(self, shapeType):
        if("rectangle" == shapeType):
            return Rectangle()
        elif("circle" == shapeType):
            return Circle()
