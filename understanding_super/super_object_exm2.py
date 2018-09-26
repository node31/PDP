from pprint import  pprint
class A(object):
    def printSuper(self):
        print(super)
        print(dir(super))
        x = super()
        print(x)
        y = super(A, self)
        print(y)
        
if __name__ == '__main__':
    a = A()
    a.printSuper()