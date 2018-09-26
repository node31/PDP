from understanding_simple_factory.CheesePizza import CheesePizza
from understanding_simple_factory.GreekPizza import GreekPizza

class SimplePizzaFactory(object):
    def createPizza(self, pizzaType):
        if(pizzaType == "cheese"):
            return CheesePizza()
        elif(pizzaType == "greek"):
            return GreekPizza()
