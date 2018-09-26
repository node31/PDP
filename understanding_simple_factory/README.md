**Why is Factory Needed ?**
Very simply put, an Object Creation in our classes mean, that we are creating dependencies on the class
of which the object is being made.

Dependencies are never good in any software design, but there will always be some, as no programs
can be written without actually creating objects.

We cannot get rid of dependencies, but we can make sure that they are minimized.

Hence, what we always want to do is follow the design principles. Factory Method strongly uses the following
design principles:
1. Code to an Interface and not to an implementation (By interfaces, we also mean AbstractClasses)
2. Dependency Inversion Principle. (i.e. your Low-Level (Object Classes) and High-Level (Behavioural Classes) should
both be dependent upon Interfaces)


What are interfaces ?
Interfaces does two things:
1. They expose to the outer world, what all the object can do.
2. It makes the objects (whoever implement that interface or extend that abstract class) to forcefully define those methods.

When, we say that Code to Interface, we mean that your logic should be present in Object Classes but the behaviour
i.e. After Method1, Method2 needs to be classes should be present in Behaviour Classes.

The dependency inversion principle says that, both of these classes should be completely separate and they should
be linked with interfaces. This makes sure that the classes are loosely coupled.


With all the factory design patterns (SimpleFactory, StaticSimpleFactory, FactoryMethod, AbstractFactory), there
is one thing which will be common. 
The code for creation of new objects will be encapsulated in one single place and that particular class
will only be responsible for the creation logic and nothing else.


We are going to understand SimpleFactory Desgin Idiom. (It is extremely common and simple)

VERY IMPORTANT: There is nothing in Python Grammar by design which supports abstract classes.
But there are modules which one can use to simulate the behavior of abstract classes.

