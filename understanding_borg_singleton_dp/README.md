**Borg Singleton Design Pattern**

In the standard singleton pattern, we only have one instance of the object.
If there are subclasses, each subclass will have a different instance, but each subclass will have the same instance

Singleton
A(Singleton)
B(Singleton)

In the above case a maximum of three different singleton objects can exist together.

Sometimes we may want to do this:
Have different instances, but each instance uses the same state i.e. the state is shared by all the instances i.e.
we have different objects, but all of them have the same shared state. 

Generally, borg singletons are better in every manner since they provide shared state. 
But, since now state is shared, care should be taken while editing it especially in multi-threading cases.

The Singleton design pattern is all about ensuring that just one instance of a certain class is ever created. 
In my experience, it is usually not a good solution to the problems it tries to solve, 
displaying different kinds of problems in different object models. 
Typically, what we really want is to let as many instances be created as necessary, but all with shared state. 
Who cares about identity? It’s state (and behavior) we care about. 
This alternate pattern to solve roughly the same problems has also been called Monostate. 
Incidentally, I like to call Singleton “Highlander”, since there can be only one.

In Python, you can implement Monostate in many ways, but the Borg design nonpattern is often best. 
Simplicity is its greatest strength. Since the __dict__ of any instance can be re-bound, 
Borg rebinds it in its __new__(or __init__) to a class-attribute dictionary. 
Now, any reference or binding of an instance attribute will actually affect all instances equally. 
I thank David Ascher for suggesting the appropriate name “Borg” for this nonpattern. 
It’s a nonpattern because it had no known uses at the time of publication: 
two or more known uses are part of the prerequisites for being a design pattern. 

The real reason that borg is different comes down to subclassing.

If you subclass a borg, the subclass' objects have the same state as their parents classes objects, 
unless you explicitly override the shared state in that subclass. 
Each subclass of the singleton pattern has its own state and therefore will produce different objects.

Also in the singleton pattern the objects are actually the same, 
not just the state (even though the state is the only thing that really matters).

The Singleton design pattern (DP) has a catchy name, but the wrong focus -- on identity rather than on state. 
The Borg design pattern has all instances share state instead, and Python makes it, literally, a snap

Borg is also known as "MonoState" or "Stateless Proxy"

One disadvantage to this method is that you can have several instances consuming memory that all know the same thing. (Not much memory, true.)