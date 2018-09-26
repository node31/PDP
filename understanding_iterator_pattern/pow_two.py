class PowTwo(object):
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    """
    Do not write iterators in this manner. The problem is as follows
    """
    a = PowTwo(10)
    i = iter(a)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    j = iter(a) # The value of n is reset.
    print(next(j))
    print(next(i)) # We have lost the iteration.

    print("-----------------------------")
    l = [1,2,3,4,5,6,7,8]
    x = iter(l)
    print(next(x))
    print(next(x))
    print(next(x))
    y = iter(l)
    print(next(y))
    print(next(x)) # The iterators of List are implemented in a better manner and hence do not become an issue.