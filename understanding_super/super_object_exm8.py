class Base(object):
    def __init__(self):
        print("Base")

class ChildA(Base):
    def __init__(self):
        print("ChildA")
        #super(ChildA, self).__init__()
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        print("ChildB")
        super(ChildB, self).__init__()

class UserDependency(Base):
    def __init__(self):
        print("UserDependency")
        super(UserDependency, self).__init__()

class UserA(ChildA, UserDependency):
    def __init__(self):
        print("UserA")
        super(UserA, self).__init__()

class UserB(ChildB, UserDependency):
    def __init__(self):
        print("UserB")
        super(UserB, self).__init__()


"""
There are two diamonds above
        Base
      /      \
ChildA        UserDependency
      \      /
        UserA
        
        Base
      /      \
ChildB        UserDependency
      \      /
        UserB        
        
MRO:
Base: [<class '__main__.Base'>, <class 'object'>]
ChildA: [<class '__main__.ChildA'>, <class '__main__.Base'>, <class 'object'>]
ChildB: [<class '__main__.ChildB'>, <class '__main__.Base'>, <class 'object'>]
UserDependency: [<class '__main__.UserDependency'>, <class '__main__.Base'>, <class 'object'>]
UserA: [<class '__main__.UserA'>, <class '__main__.ChildA'>, <class '__main__.UserDependency'>, <class '__main__.Base'>, <class 'object'>]
UserB: [<class '__main__.UserB'>, <class '__main__.ChildB'>, <class '__main__.UserDependency'>, <class '__main__.Base'>, <class 'object'>]        
       
"""

if __name__ == '__main__':
    print("Base:", Base.mro())
    print("ChildA:", ChildA.mro())
    print("ChildB:", ChildB.mro())
    print("UserDependency:", UserDependency.mro())
    print("UserA:", UserA.mro())
    print("UserB:", UserB.mro())
    print("*" * 50)
    UserA()
    print("*" * 50)
    UserB()