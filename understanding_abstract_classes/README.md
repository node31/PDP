**What are Abstract Classes**
Abstract classes have the following features:
1. They cannot be instantiated
2. They have some abstract methods, which should be implemented by any of their subclasses

In Python, by definition of grammer, there is no way to define abstract classes directly
We need to take help of module called "abc", to define abstract classes.

Now, in order to define abstract class, following is the syntax:

    class A(metaclass=abc.ABCMeta):
        pass

Now, if you try instantiating the above class, it will get instantiated. 
But, just above we said that the abstract classes should not get instantiated.
To prevent the abstract class from getting instantiated, you should have atleast one abstractmethod.

There are three different types of abstract methods
1. Abstract Methods. (They can use both instance and class variables)
2. Abstract Class Methods. (They can use class variables)
3. Abstract Static Methods. (They cannot use class or instance variables.) They are
   present there because they logically belong there. 

In order for a class to be abstract and not get instantiated, (i.e. for the class to be able to actually throw an error
at runtime, we need to have atleast of the above methods defined)

In order to make a method as:
1. Abstract method, you can use the decorator: @abc.abstractmethod
2. Abstract Class Method : @abc.abstractclassmethod
3. Abstract Static Method: @abc.abstractstaticmethod

The subclasses, should implement these abstract methods. If they do not it will not result in a COMPILE TIME ERROR
NOTE: Actually in Python, there is no compilation and hence there are no compile time errors. The errors,
which you see are syntax errors, when the Python Syntax is in-correct. 
Now, if you have not implemented the abstract methods in Python, it will not raise any kind of error.
When you actually run the code, then it will just go and execute the method which is present in the parent class.
And hence, always some default implementation will be called.

Hence, it is generally told to raise NotImplementedError from the Abstract Base classes in python so that, if a 
subclass has not implemented the method correctly and the parent method gets called, then the parent method
is going to raise that NotImplementedError
   