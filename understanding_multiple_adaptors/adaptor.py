import understanding_multiple_adaptors.turkey as turkey
import understanding_multiple_adaptors.duck as duck
import understanding_multiple_adaptors.bird as bird
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

class BirdAdaptor(duck.Duck):
    def __init__(self, bird_instance):
        if not isinstance(bird_instance, bird.Bird):
            raise Exception("Invalid Bird")
        self.bird_instance = bird_instance
        super(BirdAdaptor, self).__init__()

    def quack(self):
        self.bird_instance.chirp()

    def fly(self):
        self.bird_instance.fly()


if __name__ == '__main__':
    t = TurkeyAdaptor(turkey.WildTurkey())
    t.quack()
    t.fly()
    #t2 = TurkeyAdaptor(duck.PondDuck())

    b = BirdAdaptor(bird.Eagle())
    b.quack()
    b.fly()
    #रb2 = BirdAdaptor(duck.PondDuck())

    # b3 = BirdAdaptor(bird.Bird())
    # b3.quack()
    # b3.fly()
    