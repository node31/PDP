from understanding_factory_method.piz.Pizza import Pizza
class NYGreekPizza(Pizza):
    def __init__(self):
        super(NYGreekPizza, self).__init__(self.__class__.__name__)

    def prepare(self):
        super(NYGreekPizza, self).prepare()

    def bake(self):
        super(NYGreekPizza, self).bake()

    def cut(self):
        super(NYGreekPizza, self).cut()

    def box(self):
        super(NYGreekPizza, self).box()