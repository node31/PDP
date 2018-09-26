**SINGLETON DESIGN PATTERN**

Sometimes you only need an object which is instantiated once i.e. you need a singleton. 
For e.g.:
    1. Printers
    2. Thread Pools
    3. Caches

As a matter of fact if we have more than one of these we may run into incorrect behavior.
    
It is also possible that a particular object is resource intensive and hence we do not want it to get created
again and again. 

Thus two major reasons why Singletons are needed is as follows:
- Correctness of program. If having more than one object, can lead to incorrect behavior we should have only one object
- Efficient Utilization of Resources. If the object is resource intensive, then we should only have one object

Why can't we simply use global variables(in Java) and modules in Python ?
The following are the reasons:
- Lazy Instantiation : We want the object to be created on demand. If we use modules/global variables,
  the object will be created as soon as we start the Application. (Moreover, if that particular object is 
  resource intensive, and we end up not use that particular object, then we wasted a whole lot of resources)
  

The first and foremost thing is to stop the instantiation of the object. 
That has to be done at the point of object creation. This means that you need to play with the object creation logic
This means, that in Python we need to touch the __new__ method.

The biggest issues while implementing singleton are with Threads. If you do not make your `if and set` 
implmentation thread safe, you will run in with cases where there are more than one instances of your object
Singleton Patterns should be made thread safe.

In Java, you can simply make a method thread safe, by adding 'synchronized'  keyword. This makes sure that only
thread is able to enter that particular method block

In Python you will have to take a lock. 
self._lock = threading.lock()
with self._lock:
    # Critical section
    
This is how you can make your sections thread safe in Python.

Singleton:-> Ensures a class only has one instance and provides a global point of access to it.

SingletonPattern is a creational pattern as it involves creation of an object

SingletonPattern should be used if the following three conditions are satisfied
1. No one really owns that single-instance but it is used by all.
2. Lazy Initialization is desired
3. Global access is not provided.

Singletons are Anti-Pattern
(An anti-pattern is something which is commonly used, but should not be)
The reasons why Singleton is bad is as follows:
1. It is something like a global variable and hence it makes your code tightly coupled
2. It is makes your Unit-Testing very difficult

To understand the tight coupling, read this: [https://stackoverflow.com/questions/41752516/why-singleton-makes-coupling]
Also, you should see examples:
1. sp_exm3.py
2. sp_exm4.py
 
Basically, singletons with subclasses is never a good idea. If you are subclassing singleton classes, then you
should be very careful, because you can run in one or other kind of problems.

Pitfalls of Singleton Design Pattern
https://www.infoworld.com/article/3112025/application-development/design-patterns-that-i-often-avoid-singleton.html