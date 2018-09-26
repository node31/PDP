**Contains Interview Type Questions**


Q1: Using printA() method, print value of x of B.

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
    