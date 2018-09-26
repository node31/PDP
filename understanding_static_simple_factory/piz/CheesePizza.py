from understanding_static_simple_factory.piz.Pizza import Pizza
class CheesePizza(Pizza):
    def __init__(self):
        super(CheesePizza, self).__init__("CheesePizza")

    def prepare(self):
        super(CheesePizza, self).prepare()


    def bake(self):
        super(CheesePizza, self).bake()

    def cut(self):
        super(CheesePizza, self).cut()

    def box(self):
        super(CheesePizza, self).box()

if __name__ == '__main__':
    p = CheesePizza()
    p.prepare()
    p.bake()
    p.cut()
    p.box()
