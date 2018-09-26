import abc
class A(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def printName(self):
        print(self.name)

class B(A):
    def helloWorld(self):
        print("Hello World")

    def printName(self):
        print("This print is being called from B %s" % self.name)

if __name__ == '__main__':
    b = B("XYZ") #This throws an error, because the default __init__ is calling the super method, which expects two
    # arguments.
    b.printName()
    b.helloWorld()
