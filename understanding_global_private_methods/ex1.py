def abc():
    print("abc")

def _def():
    print("def")

def __foo():
    print("foo")

x = 5

class Bar(object):
    def f1(self):
        print("f1")

    def _f2(self):
        print("f2")

    def __f3(self):
        print("f3")



abc()
_def()
__foo()
print(x)

b = Bar()
b.f1()
b._f2()
b._Bar__f3()

