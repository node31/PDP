from understanding_static_simple_factory.piz.CheesePizza import CheesePizza
from understanding_static_simple_factory.piz.GreekPizza import GreekPizza

class SimplePizzaFactory(object):
    @staticmethod
    def createPizza(pizzaType):
        if(pizzaType == "cheese"):
            return CheesePizza()
        elif(pizzaType == "greek"):
            return GreekPizza()
