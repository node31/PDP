class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class AnimalSingleton(Borg):
    def __init__(self, species):
        print("Inside Animal Singleton")
        print(self.__dict__)
        self.species = species

if __name__ == '__main__':
    a1 = AnimalSingleton("Python")
    a2 = AnimalSingleton("Burmese Python") #This changes the state of the earlier object.

    print(a1)
    print(a2)
    print(id(a1))
    print(id(a2))
    print(a1.species)
    print(a2.species)