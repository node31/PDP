class A(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ method of A is called")
        print(cls)
        print(args)
        print(kwargs)

    def __init__(self):
        print("__init__ method of A is called")

if __name__ == '__main__':
    a1 = A()
    a2 = A(1,2, abc=3)
    print(a1) #Objects have not been instantiated
    print(a2) #Objects have not been instantiated
    print(id(a1))
    print(id(a2))
    print(id(None))