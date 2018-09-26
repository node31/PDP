import abc

class Duck(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def quack(self):
        print(self.__class__.__name__, " is quacking")

    @abc.abstractmethod
    def fly(self):
        print(self.__class__.__name__, " is flying")

class PondDuck(Duck):
    def quack(self):
        super(PondDuck, self).quack()
    def fly(self):
        super(PondDuck, self).fly()

if __name__ == '__main__':
    p = PondDuck()
    p.quack()
    p.fly()