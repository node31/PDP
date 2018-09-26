from understanding_factory_method.piz.Pizza import Pizza
class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super(ChicagoCheesePizza, self).__init__(self.__class__.__name__)

    def prepare(self):
        super(ChicagoCheesePizza, self).prepare()

    def bake(self):
        super(ChicagoCheesePizza, self).bake()

    def cut(self):
        super(ChicagoCheesePizza, self).cut()

    def box(self):
        super(ChicagoCheesePizza, self).box()
