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
    s2 = Singleton()
    print(id(s1))
    print(id(s2))
