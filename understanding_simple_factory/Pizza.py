import abc
class Pizza(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def prepare(self):
        print("Preparing %s" % self.name)

    @abc.abstractmethod
    def bake(self):
        print("Baking %s" % self.name)

    @abc.abstractmethod
    def cut(self):
        print("Cutting %s" % self.name)

    @abc.abstractmethod
    def box(self):
        print("Boxing %s" % self.name)

if __name__ == '__main__':
    print("Hello")


