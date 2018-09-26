class BetterPowTwo(object):
    """Class to implement an iterator
        of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self): #Consider this method as the method which returns an iterator object
        return BetterPowTwoIterator(self.max)

class BetterPowTwoIterator(object):
    def __init__(self, max):
        self.max = max
        self.n = 0
    def __next__(self): #Consider this method as the next method
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
if __name__ == '__main__':
    a = BetterPowTwo(10)
    i = iter(a)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    j = iter(a)  # The value is not reset as we are getting a new object
    print(next(j))
    print(next(i))