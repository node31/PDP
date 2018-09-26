**Super in Python**

We call super as follows in Python

super(X,Y).__new__(Z)
super(X,Y).__init__(Z)
super(X,Y).[Any other function call]

Let us understand what is a super ?

First and foremost we need to understand that super is a class in Python.
Unlike Java, super is not a function call. It is an object. 

When you call super(X,Y), you are making an object of class called super()
Hence, super(X,Y) is a simple object

In Python3, you can use super(). But for greater understanding, we will go with the syntax super(X,Y)

super(X,Y)
X must be of type 'type'. [type is a class in Python which extends from object]
Y should follow one of the following:
   1. Y should be instance of X i.e. isinstance(Y, X) should be true
   2. Y should be subclass of X i.e. issubclass(Y, X) should be true
either one of the above should be true for the super(X,Y) instantiation to be successful.

One of the major advantages of using super, is that you do not have to care about the BaseClass name.
Even if it get's changed the super implementation will not change.

**Understanding the arguments of super**
super(X,Y).alpha()
X is a type.
The MRO of X is computed. 
Suppose MRO of X is as follows: [X, a, b, c, d]
Now, the method which needs to be called alpha is searched in all the classes.
Wherever the method alpha is first found, that particular implementation of the method is returned. 

Now, we do not know what kind of method is alpha. Alpha can be:
- Instance Method
- Class Method
- Static Method

According to the type of method alpha is, we need to pass the Y argument.
If alpha is 
- Instance method, then Y should be of the type 'self'
- Class method, then Y should be of the type 'cls'
- Static method. Y can be of any type. It does not matter.

Thus, from the above we realize that super is heavily related with MRO.
MRO is differently calculated in old and new-style classes. We should always use new-style classes for
better MRO calculation

Hence, super is extremely simple. 
1. Super finds out MRO
2. Then super traverses the MRO to find the first class which has the function needed
3. The second argument of super comes into play as the function is passed that argument (if it is a class or instance method)
[The above logic i.e. Step 3 is true is shown in Example called super_object_exm6.py]
4. That particular function is then called. 


References:
https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods [READ THIS IMPORTANT]
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
https://stackoverflow.com/questions/9056955/what-does-super-in-new
