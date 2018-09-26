import abc
class Color(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fill(self):
        print("%s is filled" % self.__class__.__name__)
class Red(Color):
    def fill(self):
        super(Red, self).fill()
class Blue(Color):
    def fill(self):
        super(Blue, self).fill()