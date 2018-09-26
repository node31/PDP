def abc():
    print("abc")

def _def():
    print("def")

def __foo():
    print("foo")

a = 5

class Bar(object):
    def x1(self):
        print("x1")
        abc()

    def x2(self):
        print("x2")
        _def()

    def x3(self):
        print("x3")
        #__foo()

        print(locals())
        print(globals())

b = Bar()
b.x1()
b.x2()
b.x3()


