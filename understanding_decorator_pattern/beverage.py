import abc


class Beverage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_cost(self):
        raise NotImplementedError


class DarkRoast(Beverage):
    def __init__(self):
        self.cost = 100
        super(DarkRoast, self).__init__()

    def get_cost(self):
        return self.cost


class HouseBlend(Beverage):
    def __init__(self):
        self.cost = 200
        super(HouseBlend, self).__init__()

    def get_cost(self):
        return self.cost
