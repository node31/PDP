from pprint import pprint
class A(object):
    def printSuper(self):
        print(super)
        pprint(dir(super))

if __name__ == '__main__':
    a = A()
    a.printSuper()