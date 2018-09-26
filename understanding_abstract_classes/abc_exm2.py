import abc
class A(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def printName(self):
        print(self.name)

if __name__ == '__main__':
    a = A("Hello") #The class instantiation does not happen.
    a.printName()