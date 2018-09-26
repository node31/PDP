from understanding_factory_method.piz.PizzaStore import PizzaStore
from understanding_factory_method.piz.ChicagoGreekPizza import ChicagoGreekPizza
from understanding_factory_method.piz.ChicagoCheesePizza import ChicagoCheesePizza
class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, pizzaType):
        if("cheese" == pizzaType):
            return ChicagoCheesePizza()
        elif("greek" == pizzaType):
            return ChicagoGreekPizza()