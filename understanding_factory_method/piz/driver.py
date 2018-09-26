from understanding_factory_method.piz.NYPizzaStore import NYPizzaStore
from understanding_factory_method.piz.ChicagoPizzaStore import ChicagoPizzaStore
if __name__ == '__main__':
    nyps = NYPizzaStore()
    cps = ChicagoPizzaStore()
    nyps.orderPizza("cheese")
    nyps.orderPizza("greek")
    cps.orderPizza("cheese")
    cps.orderPizza("greek")