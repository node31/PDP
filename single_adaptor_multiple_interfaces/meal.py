import abc
class Meal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getMeal(self):
        print("%s prepared" % self.__class__.__name__)
    @abc.abstractmethod
    def cleanDishes(self):
        print("%sDishes cleaned" % self.__class__.__name__)

class Lunch(Meal):
    def getMeal(self):
        super(Lunch, self).getMeal()

    def cleanDishes(self):
        super(Lunch, self).cleanDishes()

if __name__ == '__main__':
    l1 = Lunch()
    l1.getMeal()
    l1.cleanDishes()