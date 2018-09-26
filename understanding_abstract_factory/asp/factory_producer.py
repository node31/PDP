from understanding_abstract_factory.asp.color import ColorFactory
from understanding_abstract_factory.asp.shape import ShapeFactory
class FactoryProducer(object):
    @staticmethod
    def getASF(factoryType):
        if "color" == factoryType:
            return ColorFactory()
        elif "shape" == factoryType:
            return ShapeFactory()

if __name__ == '__main__':
    fp = FactoryProducer.getASF("color")
    r = fp.getColor("red")
    b = fp.getColor("blue")
    r.fill()
    b.fill()
    fp = FactoryProducer.getASF("shape")
    r = fp.getShape("rectangle")
    c = fp.getShape("circle")
    r.draw()
    c.draw()