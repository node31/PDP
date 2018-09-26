class Singleton(object):
    __INSTANCE = None
    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__INSTANCE

    def __init__(self):
        self.x = 10

if __name__ == '__main__':
    s1 = Singleton()
    print(s1.x)
    s1.x = 30
    s2 = Singleton()
    print(s2.x) #-->The __init__ instantiation is happening again.
    # Hence, whenever you make an object and __init__ is called, the state will be changed back again.
    # You should be very careful while using singletons.
