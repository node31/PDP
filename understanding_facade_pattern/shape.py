import abc
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        print("%s drawing" % self.__class__.__name__)

class Square(Shape):
    def draw(self):
        super(Square, self).draw()
class Circle(Shape):
    def draw(self):
        super(Circle, self).draw()

if __name__ == '__main__':
    Square().draw()