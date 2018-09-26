class MenuItem(object):
    def __init__(self, name, price, veg):
        self.name = name
        self.price = price
        self.veg = veg

    def __str__(self):
        return ("[Menu Item: %s %s %s]" % (self.name, self.price, self.veg) )

