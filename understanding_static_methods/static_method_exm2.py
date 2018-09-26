class A(object):
    def __init__(self):
        self.x = 10

    def printA(self):
        print(self.x)

class B(object):
    def __init__(self):
        self.x = 20

if __name__ == '__main__':
    b1 = B()
    A.printA(b1) # 20 gets printed.