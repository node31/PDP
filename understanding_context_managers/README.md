Context Managers allow you to allocate and release resources precisely when you want to.

The most widely used example of context managers is the with statement

Suppose you have two releated pair of operations which you want to do with a block of code
in between them. Context Managers will allow us to do specifically that.

    with open("a.txt", "w") as f:
        f.write("Hola")
        
    
    
    f = open("a.txt", "w");
    try:
        f.write("Hola")
    finally:
        f.close()

Context Managers also help us to remove boilerplate code
Common Uses of Context Managers
1. File Open/Close
2. Locking/Unlockig
3. DB Connection Open/Close

There are three ways in which context managers can be used
1. Class
2. Generator
3. Decorator

We will explore all of them one by one

Context Managers by class.
If you want to make sure that your class supports the ContextManager protocol, you need to do the following things
1. Implement the __enter__(self) method
2. Implement the __exit__(self, type, value, traceback)

1. The with statement stores the __exit__ method of the class whose object is returned by __enter__ method
2. It calls the __enter__ method of the object which is given to it
3. __enter__ method opens the file and returns it.
4. the opened file handle is passed to opened_file.
5. we write to the file using .write()
6. with statement calls the stored __exit__ method.
7. the __exit__ method closes the file.
