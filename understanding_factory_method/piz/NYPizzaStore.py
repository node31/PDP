from understanding_factory_method.piz.PizzaStore import PizzaStore
from understanding_factory_method.piz.NYGreekPizza import NYGreekPizza
from understanding_factory_method.piz.NYCheesePizza import NYCheesePizza
class NYPizzaStore(PizzaStore):
    def createPizza(self, pizzaType):
        if("cheese" == pizzaType):
            return NYCheesePizza()
        elif("greek" == pizzaType):
            return NYGreekPizza() 