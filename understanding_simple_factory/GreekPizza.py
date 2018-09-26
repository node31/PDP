from understanding_simple_factory.Pizza import Pizza
class GreekPizza(Pizza):
    def __init__(self):
        super(GreekPizza, self).__init__("GreekPizza")

    def prepare(self):
        super(GreekPizza, self).prepare()

    def bake(self):
        super(GreekPizza, self).bake()

    def cut(self):
        super(GreekPizza, self).cut()

    def box(self):
        super(GreekPizza, self).box()