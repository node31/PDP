class A(object):
    def ab_print(self, a, b):
        print("ab_print_method")
        print(a)
        print(b)
        print("*" * 50)

class B(object):
    @staticmethod
    def ab_print(a,b):
        print("ab_print_method")
        print(a)
        print(b)
        print("*" * 50)

if __name__ == '__main__':
    a1 = A()
    a1.ab_print(3,4)

    try:
        A.ab_print(5,6) #This will fail as the first argument is not of type A. It is of type int
    except Exception as ex:
        print(ex)

    b1 = B()
    try:
        b1.ab_print(7,8) # This does not fail. This is because, you can call static methods via class or objects.
    except Exception as ex:
        print(ex)

    B.ab_print(9,10)
    try:
        A.ab_print(b1, 11, 12) #Excpected object was of type A. We got an object of type B
    except Exception as ex:
        print(ex)
