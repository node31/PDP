import abc
class Turkey(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gobble(self):
        print(self.__class__.__name__," is gobbling")
    @abc.abstractmethod
    def fly(self):
        print(self.__class__.__name__," is flying")

class WildTurkey(Turkey):
    def gobble(self):
        super(WildTurkey, self).gobble()

    def fly(self):
        super(WildTurkey, self).fly()

if __name__ == '__main__':
    t = WildTurkey()
    t.gobble()
    t.fly()