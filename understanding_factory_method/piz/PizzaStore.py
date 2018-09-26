import abc
class PizzaStore(metaclass=abc.ABCMeta):
    def orderPizza(self, pizzaType):
        p = self.createPizza(pizzaType)
        p.prepare()
        p.bake()
        p.cut()
        p.box()

    @abc.abstractmethod
    def createPizza(self, pizzaType):
        raise NotImplementedError

