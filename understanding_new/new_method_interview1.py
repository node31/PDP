#Given, two classes A and B, how do you modify class A, so that it returns object of B upon instantiaion

class A(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ method of A")
        return super(A, cls).__new__(B, *args, **kwargs)

    def __init__(self):
        print("__init__ method of A")

    def amethod(self):
        print("This is method of A")

class B(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ method of B")
        return super(B, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print("__init__ method of B")

    def bmethod(self):
        print("This is method of B")

if __name__ == '__main__':
    a = A() # For all purposes this is object of B. In this case __init__ method of neither A nor B was called.
    # This is because A, tried to call the __init__ method, but it did not find it in class A. which accepts
    # object B as the first argument
    print(a)
    try:
        a.amethod()
    except Exception as ex:
        print(ex)

    try:
        a.bmethod()
    except Exception as ex:
        print(ex)

    b = B()
