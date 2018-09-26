class A(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ method of A is called")
        print(cls)
        print(args)
        print(kwargs)
        instance = object.__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, *args, **kwargs):
        print("__init__ method of A is called")

if __name__ == '__main__':
    a1 = A()
    a2 = A(1,2, abc=3)
    print(a1)
    print(a2)
    print(id(a1))
    print(id(a2))
    print(id(None))