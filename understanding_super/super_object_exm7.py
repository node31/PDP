class A(object):
    @classmethod
    def someClassMethod(cls):
        print("Class Method of A")
        print(cls.X) #This implementation is bad, but it puts forward the point which I am trying to make
        # The point which I am trying to make is that the cls, which is passed here is of type B and and not of type A

class B(A):
    X = 10
    @classmethod
    def someClassMethod(cls):
        X = 20 #Local Variable
        print("Class Method of B")
        super(B, cls).someClassMethod()

if __name__ == '__main__':
    B.someClassMethod()
