This is the FactoryMethod Pattern
It is one of the most useful and extensible patterns. 

It is not so common, but it is a good pattern.
Here the responsibility of object instantiation is passed to the subclass. That object creates the actual object
and the superclass then uses that object for the actual actions.

Superclass does not know what is the type of subclass which was generated. It is relying on the fact that 
whatever object the subclass returns will adhere to the interface and hence all the required methods will be
present.