import abc
class Ing(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def obtainIngredients(self):
        print("%s is obtaining ingredients" % self.__class__.__name__)

class Chotu(Ing):
    def obtainIngredients(self):
        super(Chotu, self).obtainIngredients()