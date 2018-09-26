import abc
class Diswasher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cleanDishes(self):
        print("%s is cleaning dishes" % self.__class__.__name__)

class IFBDishwaser(Diswasher):
    def cleanDishes(self):
        super(IFBDishwaser, self).cleanDishes()

if __name__ == '__main__':
    d = IFBDishwaser()
    d.cleanDishes()