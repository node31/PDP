import abc
class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getColor(self, colorType):
        raise NotImplementedError

    @abc.abstractmethod
    def getShape(self, shapeType):
        raise NotImplementedError

