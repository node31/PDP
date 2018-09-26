import abc
from understanding_decorator_pattern.beverage import Beverage


class CondimentType(object):
    MOCHA = 0
    SOY = 1
    WHIP = 2


class CondimentStore(object):
    @staticmethod
    def getCondiment(condimentType, b):
        if CondimentType.MOCHA == condimentType:
            print("THIS IS MOCHA")
            return Mocha(b)
        elif CondimentType.SOY == condimentType:
            print("THIS IS SOY")
            return Soy(b)
        elif CondimentType.WHIP == condimentType:
            print("THIS IS WHIP")
            return Whip(b)
        print("THIS IS NONE TYPE OBJECT")
        return None


class Condiment(Beverage, metaclass=abc.ABCMeta):
    def __init__(self, b):
        if not isinstance(b, Beverage):
            raise Exception("b is not an instance of Beverage")
        self.b = b

    @abc.abstractmethod
    def get_cost(self):
        raise NotImplementedError

    @staticmethod
    def getBeverageWithAddedCondiment(condimentType, b):
        return CondimentStore.getCondiment(condimentType, b)


class Mocha(Condiment):
    def __init__(self, b):
        self.cost = 10
        super(Mocha, self).__init__(b)

    def get_cost(self):
        return self.cost + self.b.get_cost()


class Soy(Condiment):
    def __init__(self, b):
        self.cost = 20
        super(Soy, self).__init__(b)

    def get_cost(self):
        return self.cost + self.b.get_cost()


class Whip(Condiment):
    def __init__(self, b):
        self.cost = 30
        super(Whip, self).__init__(b)

    def get_cost(self):
        return self.cost + self.b.get_cost()
