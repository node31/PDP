from understanding_simple_factory.SimplePizzaFactory import SimplePizzaFactory
class PizzaStore(object):
    def __init__(self):
        self.spf = SimplePizzaFactory()
    def orderPizza(self, pizzaType):
        p = self._createPizza(pizzaType)
        p.prepare()
        p.bake()
        p.cut()
        p.box()

    def _createPizza(self, pizzaType):
        return self.spf.createPizza(pizzaType)

if __name__ == '__main__':
    ps = PizzaStore()
    ps.orderPizza("cheese")
    ps.orderPizza("greek")