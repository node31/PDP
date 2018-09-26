import abc
from understanding_abstract_factory.asp.abstract_factory import AbstractFactory

class Color(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fill(self):
        raise NotImplementedError

class Red(Color):
    def fill(self):
        print("Filling with %s" % self.__class__.__name__)

class Blue(Color):
    def fill(self):
        print("Filling with %s" % self.__class__.__name__)

class ColorFactory(AbstractFactory):
    def getColor(self, colorType):
        if("red" == colorType):
            return Red()
        elif("blue" == colorType):
            return Blue()

    def getShape(self, shapeType):
        raise NotImplementedError