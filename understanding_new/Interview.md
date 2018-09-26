**Contains Interview Type Questions**

Q1: Given the blueprint of two class B, write class A such that it upon instantiation of A(), object B is returned

#Question-->

    class A(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of A")
            # Write code here
            
        def __init__(self, *args, **kwargs):
            print("__init__ method of A")
    
        def amethod(self):
            print("This is method of A")
    
    
    class B(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of B")
            pass
    
        def __init__(self, *args, **kwargs):
            print("__init__ method of B")
            
    
#Answer-->
        
    class A(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of A")
            # Write code here
            instance = object.__new__(B, *args, **kwargs)
            instance.__init__(*args, **kwargs)
            return instance
            
        def __init__(self, *args, **kwargs):
            print("__init__ method of A")
    
        def amethod(self):
            print("This is method of A")
    
    
    class B(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of B")
            pass
    
        def __init__(self, *args, **kwargs):
            print("__init__ method of B")
            

Q2: Given the blueprint of two class B, write class A such that it upon instantiation of A(), object B is returned
See carefully, the blueprint has changed

#Question-->

    class A(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of A")
            # Write code here
            
        def __init__(self, *args, **kwargs):
            print("__init__ method of A")
    
        def amethod(self):
            print("This is method of A")
    
    
    class B(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of B")
            return super(B, cls).__new__(cls, *args, **kwargs)
    
        def __init__(self, *args, **kwargs):
            print("__init__ method of B")
            
    
#Answer-->
        
    class A(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of A")
            # Write code here
            return B()
            
        def __init__(self, *args, **kwargs):
            print("__init__ method of A")
    
        def amethod(self):
            print("This is method of A")
    
    
    class B(object):
        def __new__(cls, *args, **kwargs):
            print("__new__ method of B")
            pass
    
        def __init__(self, *args, **kwargs):
            print("__init__ method of B")            