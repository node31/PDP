import abc
from implmenting_coffee_with_factory_pattern.condiment import Condiment


class Bevrage(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__condimentList__ = list()

    def _getCondimentCost(self):
        cost = 0
        for condiment in self.__condimentList__:
            cost += condiment.getCost()
        return cost

    def addCondiment(self, condimentType):
        self.__condimentList__.append(Condiment.getCondiment(condimentType))

    @abc.abstractmethod
    def getCost(self):
        raise NotImplementedError


class DarkRoast(Bevrage):
    def __init__(self):
        self.cost = 100
        super(DarkRoast, self).__init__()

    def getCost(self):
        return self.cost + super(DarkRoast, self)._getCondimentCost()


class HouseBlend(Bevrage):
    def __init__(self):
        self.cost = 200
        super(HouseBlend, self).__init__()

    def getCost(self):
        return self.cost + super(HouseBlend, self)._getCondimentCost()
