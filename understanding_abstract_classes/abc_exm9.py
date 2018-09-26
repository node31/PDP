import abc
class A(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def printName(self):
        print("PRINT METHOD OF A %s" % self.name)

class B(A):
    def printName(self):
        print("This print is being called from B %s" % self.name)
        super(B, self).printName()

class C(A):
    def printName(self):
        print("This print is being called from C %s" % self.name)
        super(C, self).printName()

if __name__ == '__main__':
    b = B("YO")
    b.printName()
    c = C("OY")
    c.printName()
