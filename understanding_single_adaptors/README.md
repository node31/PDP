**Adaptor Patterns**

These patterns adapt one interface to other interface. That is all what this pattern does

Imagine a scenario, where you have written a lot of classes using one kind of interface.
Now, you want to use some classes which have been supplied by the vendor. The issue is that vendor has used
some different kind of interface. 

Now, you cannot go and change your interface, since a large number of classes are using that. 
You should not be creating a new interface since then the functionality in your system will be divided in a manner
that some classes are using the interface which you implemented and some classes are using the interface which 
the vendor implemented. 
Obviously you cannot change the vendor interface.

NOTE: Adaptor pattern comes in two flavors object adaptors and class adaptors.
NOTE: In object adaptors, functionality is achieved by composition
NOTE: In class adaptors functionality is achieved by inheritance (multiple inheritance is required)
NOTE: Since, we favor composition over inheritance and not all languages support multiple inheritance, we are just going
to study object adaptors. 
Here comes the Adaptor Pattern. We are going to study three different adaptor patterns
1. Single Adaptors --> The Adaptor translates the one interface to other interface
2. Multiple Adaptors --> These are simply multiple single adaptors but they show the point more clearly
3. SingleAdaptorForMultipleInterfaces --> This is a good example, where you have a single functionality, but the vendor had
broken the functionality into multiple pieces.

Now, let us understand these adaptors a bit more in detail
1. Single Adaptors
They translate interfaces
You have an interface X. Lot of the classes follow interface X.
Now, you need some functionality from a class called A which implements interface Y. {Classes A and Y are supplied by some
external vendor and their functionality cannot be changed}.
Everytime you neeed to convert the requests of methods of X to that of type of Y.
We need to have an AdaptorClass in between.
The adaptor class will be called YAdaptor and will implement interface X, and will be composed of object which implements Y.

The class diagram will be as follows

--->> : COMPOSITION
---> : INHERITANCE
CLIENT --->> X                                     Y   Y
             ^                                     ^   ^
             |                                     |   |
             |                                     |   |
             YAdaptor --->> Y                      A   B
             
At runtime you can decide what kind of object is required in the YAdaptor. Object of type A or type B

2. Multiple Adaptors
These are simply multiple single adaptors. They are important because they relay the point more clearly and hence we are
going to study them

CLIENT --->> X

 X                                     Y   Y
 ^                                     ^   ^
 |                                     |   |
 |                                     |   |
 YAdaptor --->> Y                      A   B
 
 X                                     Z   Z
 ^                                     ^   ^
 |                                     |   |
 |                                     |   |
 ZAdaptor --->> Z                      M   N
 
 So, if there were no adaptors, then you would have to implement two new interfaces and everytime you would want to use 
 one of the methods, of Y or Z, you would have to remember those. Moreover, the methods of Y or Z would have been spread
 all over the place which is maintenance nightmare. So, instead of that we did a simple fix. We introduced adaptors.
 Now, the methods of Y and Z are contained in their respective adaptors and only methods of X are scattered all over the place
 
3. SingleAdaptorForMultipleInterfaces
Now, sometimes it is possible that you need to have multiple classes inside your adaptor. This is because you need to achieve 
the functionality obtained by your class, by different vendor classes. The diagram will look like this:

CLIENT --->> X
 X                                     Y   Y   Z  Z
 ^                                     ^   ^   ^  ^
 |                                     |   |   |  |
 |                                     |   |   |  |
 YZAdaptor --->> Y                     A   B   M  N
           --->> Z

People often misunderstand SingleAdaptorForMultipleInterfaces as FacadePattern because they look similar.
Indeed, they are similar looking but are extremely different. 
           
They are different in intent.
Facade patterns are present to simplify the underlying subsystem interfaces. They are used to achieve loose coupling and
principle of lease knowledge(LAW of DEMETER) i.e. the client should not have much knowledge about the systems underneath
Adaptor patterns are used to convert one kind of interface to other.
Facade patterns are used to simplify the interfaces.

 