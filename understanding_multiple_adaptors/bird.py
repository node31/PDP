import abc

class Bird(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def chirp(self):
        print(self.__class__.__name__, " is chirping")

    @abc.abstractmethod
    def fly(self):
        print(self.__class__.__name__, " is flying")

class Eagle(Bird):

    def chirp(self):
        super(Eagle, self).chirp()

    def fly(self):
        super(Eagle, self).fly()

if __name__ == '__main__':
    e = Eagle()
    e.chirp()
    e.fly()