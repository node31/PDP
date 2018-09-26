class A(object):
    def someMethod(self):
        print("Some Method of A")
        print(self.x) #This implementation is bad, but it puts forward the point which I am trying to make
        # The point which I am trying to make is that the self, which is passed here is of type B and and not of type A

class B(A):
    def __init__(self, x):
        self.x = x

    def someMethod(self):
        print("Some Method of B")
        super(B, self).someMethod()

if __name__ == '__main__':
    b = B(25)
    b.someMethod()

    try:
        a = A()
        a.someMethod() #This will result in an error as A does not have a variable called x.
    except Exception as ex:
        print(ex)
