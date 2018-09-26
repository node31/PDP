class A(object):
    def printSuper(self):
        x = super()
        y = super(A, self)
        z = super(A, A())
        u = super(object, A())
        w = super(object, object())
        l = [x,y,z,u,w]
        for o in l:
            print(o)

        print("*" * 50)
        b = super(A, A)
        print(b)


if __name__ == '__main__':
    a = A()
    a.printSuper()