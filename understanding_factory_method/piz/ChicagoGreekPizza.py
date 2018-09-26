from understanding_factory_method.piz.Pizza import Pizza
class ChicagoGreekPizza(Pizza):
    def __init__(self):
        super(ChicagoGreekPizza, self).__init__(self.__class__.__name__)

    def prepare(self):
        super(ChicagoGreekPizza, self).prepare()

    def bake(self):
        super(ChicagoGreekPizza, self).bake()

    def cut(self):
        super(ChicagoGreekPizza, self).cut()

    def box(self):
        super(ChicagoGreekPizza, self).box()