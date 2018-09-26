from understanding_factory_method.piz.Pizza import Pizza
class NYCheesePizza(Pizza):
    def __init__(self):
        super(NYCheesePizza, self).__init__(self.__class__.__name__)

    def prepare(self):
        super(NYCheesePizza, self).prepare()

    def bake(self):
        super(NYCheesePizza, self).bake()

    def cut(self):
        super(NYCheesePizza, self).cut()

    def box(self):
        super(NYCheesePizza, self).box()
