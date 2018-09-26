class A(object):
    def someMethod(self):
        print("Some Method of A")

class B(A):
    def someMethod(self):
        print("Some Method of B")
        super(B, self).someMethod()

if __name__ == '__main__':
    b = B()
    b.someMethod()