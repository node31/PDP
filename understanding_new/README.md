
**New Style Classes in Python**

In this directory all information which concerns __new__ method is being described
Also, the examples are given separately.

**Prequistes**

- Static Methods (understanding_static_methods)

*What creates the object ?*
Method __new__ creates the object

*What is __new__ ?*

- __new__ is a static method which creates an instance.
- It is not instance method, because instance is not created yet
- __new__ gets called when you call the class. Calling the class is similar to calling a method
- __new__ must return the created object
- Only when __new__ returns the created object then __init__ gets called.
- If __new__ does not return an instance then __init__ would not be called
- __new__ is always called before __init__ 
- __new__ gets passed all the arguments which we pass during object creation
- Along with that __new__ also gets the class, of which the object needs to be created

The logic for object creation is present in the __new__ method of object class

When we do not return anything from the __new__ method, python implicitly returns
None

You should call object.__new__(cls, *args, **kwargs) in your implementation.
But the above will work only if you are directly inheriting from object

If you are inheriting from SomeClass X, then you should call X.__new__(cls, *args, **kwargs)
This all works great and is great if you have single inheritance.

But if you have multiple inheritance, then you do not know the MRO (i.e. Method Resolution Order)
and which class is next in that order. So you should always call __new__ like this
super(CurrentClassName, cls).__new__(cls, *args, **kwargs)

Please read this:
http://agiliq.com/blog/2012/06/__new__-python/
