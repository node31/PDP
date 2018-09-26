**Static Methods in Python**

Python supports 4 kinds of functions/methods

- Functions : These are defined outside classes
- Static Methods: These are defined inside classes. They do not use any class variables or instance variables. They can be functions as well. They are defined inside classes because they have logical connection with the class. Static methods do not receive class or instance upon call
- Class Methods: These are defined inside classes. They have logical connection to the class and use the class variables defined. They receive the class object upon call.
- Instance Methods: These are defined inside classes. They have logical connection to the class. They use both the class variables and instance variables. They receive the instance object upon call.

When a method is defined inside a class,
by default it is an instance method. 

This means that by default whenever that method
is called, the first argument which will be given
to the method will be of the type of object of that class.
This is done by default in Python Interpreter

To remove the above functionality, we need to make the 
methods explicitly class-methods or static-methods

To make a method class-method, you need to
specify @clsmethod
To make a method static-method, you need to 
specify @staticmethod

When you do @clsmethod, this instructs the Python
interpreter to pass the class object as the first argument

When you do @staticmethod, this instructs the Python
interpreter to not pass anything to the method. 

Read the following answer as well:
https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

