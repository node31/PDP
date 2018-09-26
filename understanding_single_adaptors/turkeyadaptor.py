import understanding_single_adaptors.turkey as turkey
import understanding_single_adaptors.duck as duck

class TurkeyAdaptor(duck.Duck):

    def __init__(self, turkey_instance):
        if not isinstance(turkey_instance, turkey.Turkey):
            raise Exception("Invalid Turkey")
        self.turkey_instance = turkey_instance
        super(TurkeyAdaptor, self).__init__()

    def quack(self):
        self.turkey_instance.gobble()

    def fly(self):
        for i in range(5):
            self.turkey_instance.fly()

if __name__ == '__main__':
    t = TurkeyAdaptor(turkey.WildTurkey())
    t.quack()
    t.fly()
    #t2 = TurkeyAdaptor(duck.PondDuck())