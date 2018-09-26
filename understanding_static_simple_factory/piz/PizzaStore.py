from understanding_static_simple_factory.piz.SimplePizzaFactory import SimplePizzaFactory
class PizzaStore(object):
    def orderPizza(self, pizzaType):
        p = self._createPizza(pizzaType)
        p.prepare()
        p.bake()
        p.cut()
        p.box()

    def _createPizza(self, pizzaType):
        return SimplePizzaFactory.createPizza(pizzaType)

if __name__ == '__main__':
    ps = PizzaStore()
    ps.orderPizza("cheese")
    ps.orderPizza("greek")