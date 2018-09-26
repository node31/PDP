class Borg(object):
    _shared_state = {}
    def __init__(self):
        self.__dict__ = Borg._shared_state

class Base1(Borg):
    def printDict(self):
        print(self.__dict__)

class Base2(Borg):
    def printDictionary(self):
        print(self.__dict__)

    def __init__(self):
        super(Base2, self).__init__()

if __name__ == '__main__':
    b1 = Base1()
    b2 = Base2()
    print(dir(b1))
    print(dir(b2))
    print(b1)
    print(b2)
    b1.printDict()
    b2.printDictionary()
    b1.x = 10
    b1.printDict()
    b2.printDictionary()
    print(b2.x)