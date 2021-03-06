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

if __name__ == '__main__':
    pass #unless you call the object of B, there is no way Python is going to raise an error.
    #Python is going to raise an error, when you 
