**Iterator Pattern**
In Python it is generally referred to as iteration protocol.

Any class which implements the __iter__ and __next__ methods follow the iteration protocol
To get an iterator of that class, you have to call iter(reference_to_object). This returns you an iterator.
When you want to go to the next object of that iterator, you call the .next() method on the iterator reference.

That is how simple loops work.