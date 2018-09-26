class Polygon(object):
    def __init__(self, id):
        print("Init of Polygon")
        self.id = id

class Rectangle(Polygon):
    def __init__(self, id):
        print("INIT of rectangle")
        print(self.__class__)
        print(self.__class__.__mro__) # (<class '__main__.Square'>, <class '__main__.Rectangle'>, <class '__main__.Polygon'>, <class 'object'>)
        super(self.__class__, self).__init__(id) # This again calls constructor of the Rectangle class

class Square(Rectangle):
    pass

if __name__ == '__main__':
    s = Square('a')