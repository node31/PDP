import abc
class Chef(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def prepareFood(self):
        print("%s is preparing food" % self.__class__.__name__)

class ExpensiveChef(Chef):
    def prepareFood(self):
        super(ExpensiveChef, self).prepareFood()