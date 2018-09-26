import implmenting_coffee_with_factory_pattern.beverage as bev
from implmenting_coffee_with_factory_pattern.condiment import CondimentType
if __name__ == '__main__':
    b = bev.HouseBlend()
    print(b.getCost())

    b = bev.DarkRoast()
    print(b.getCost())
    b.addCondiment(CondimentType.MOCHA)
    print(b.getCost())
    b.addCondiment(CondimentType.SOY)
    print(b.getCost())
    b.addCondiment(CondimentType.MOCHA)
    print(b.getCost())
    b.addCondiment(CondimentType.WHIP)
    print(b.getCost())