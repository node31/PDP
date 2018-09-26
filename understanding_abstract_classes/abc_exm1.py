import abc
class A(metaclass=abc.ABCMeta):

    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)


if __name__ == '__main__':
    a = A("YOYO") #Abstract classes can get instantiated, since there are no abstract methods which are present.
    #To make sure that abstract classes do not get instantiated, we need to have atleast one abstract method.
    a.printName()