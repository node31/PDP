import understanding_decorator_pattern.beverage as bev
from understanding_decorator_pattern.condiment import Condiment, CondimentType
if __name__ == '__main__':
    b = bev.DarkRoast()
    print(b.get_cost())

    b = bev.HouseBlend()
    print(b.get_cost())
    b = Condiment.getBeverageWithAddedCondiment(CondimentType.MOCHA, b)
    print(b.get_cost())
    b = Condiment.getBeverageWithAddedCondiment(CondimentType.WHIP, b)
    print(b.get_cost())
    b = Condiment.getBeverageWithAddedCondiment(CondimentType.MOCHA, b)
    print(b.get_cost())
    b = Condiment.getBeverageWithAddedCondiment(CondimentType.SOY, b)
    print(b.get_cost())
