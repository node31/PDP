import abc
class CondimentType(object):
    MOCHA = 0
    SOY = 1
    WHIP = 2

class CondimentStore(object):
    @staticmethod
    def getCondiment(condimentType):
        if CondimentType.MOCHA == condimentType:
            return Mocha()
        elif CondimentType.SOY == condimentType:
            return Soy()
        elif CondimentType.WHIP == condimentType:
            return Whip()
        raise Exception("Unknown Type")

class Condiment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getCost(self):
        raise NotImplementedError

    CS = CondimentStore()
    @staticmethod
    def getCondiment(condimentType):
        return Condiment.CS.getCondiment(condimentType)

class Mocha(Condiment):
    def __init__(self):
        self.cost = 10
    def getCost(self):
        return self.cost

class Soy(Condiment):
    def __init__(self):
        self.cost = 20
    def getCost(self):
        return self.cost

class Whip(Condiment):
    def __init__(self):
        self.cost = 30
    def getCost(self):
        return self.cost
