**Decorator Pattern**
This pattern is used, when you want to add behaviour to an object at runtime. It is a very powerful design pattern

Very powerful principles arise from this particular design pattern.

1. Open-Close Principle: Code should be open for extension but closed for modification.
We should be coding/designing in such a manner that it is open for extension i.e. you can add new classes/interfaces etc,
but it should be closed for modification i.e. the exisiting code should work without making any changes. 
This can be easily achieved by Decorator Pattern
This can be heavily achieved by Decorator Pattern and by heavily I mean, literllay that is what decorator pattern actually does

2. Favour composition over inheritance
First, we need to understand why this is important
We should do inheritance only when there exists "IS-A" relationship. If there is any other kind of relationship, we
should try avoiding inheritance.
Composition is helpful, because you can add fuctionality to your class at runtime. 
Let's understand this with help of an example

Let's say we have 4 classes, A,B,C,D
The classes C & D inherit from B i.e. they look like this:

        B
      /   \
     C     D
 
Now, we have a class "A".
Suppose we want some functionality of B to be present in A.
If we inherit from B, then we will get all the functionality of B, which is great. That is what we wanted. 
But, if we compose B in A, i.e. A has a reference of B, then we can do so much more. We can have functionality of
C or D, inside A during runtime, which is kind of more than what inheritance could ever achieve. 
Hence, we always try to favor composition over inheritance.



Whenever, you want to add functionality at runtime always think of a decorator pattern.
Singleton and Factory patterns are creational patterns. Decorator is a behavioural pattern i.e. it ADDs some behavior
at runtime. 

NOTE: Decorator patterns are generally used with Factory Patterns. So, try to generally see, if you are using one,
can you use the other. 
NOTE: Decorator patterns and decorators in Python are widely different concepts. DO NOT INTERMIX them.
NOTE: Decorators are widely different from ANNOTATIONS in Java (We will cover this, in understanding decorators section)


Now, let us see what the decorator pattern actually is:

There are two parts of the decorator pattern:
1. The thing which needs to be decorated
2. The thing which decorates.

Now, there are two behaviours which enable decoration:
1. The thing which needs to be decorated and the thing which decorates, should be of same type i.e. they should
extend from same interface/class i.e. there should be a superclass which can be used to refer them both.
2. The thing which decorates, should have a reference of that superclass. This will allow us to use the functionality of superclass
{
BUT WE ARE ALREADY INHERITING, WHY DO WE NEED A REFERENCE OF THE SUPERCLASS
WE ARE INHERITING SO THAT WE CAN USE THE SAME REFERENCE. INHERITING IN THIS CASE IS USED ONLY FOR MAKING IT SIMILAR
TO THE OBJECT WHICH NEEDS TO BE DECORATED.
HAVING A REFERENCE ACTUALLY ALLOWS US TO CALL THE BEHAVIOUR OF SUPERCLASS.
}

