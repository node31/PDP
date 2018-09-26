class A(object):
    def __new__(cls, *args, **kwargs):
        x = super(A, cls)
        print(x)
        print(dir(x))
        print(x.__mro__)

if __name__ == '__main__':
    a = A()