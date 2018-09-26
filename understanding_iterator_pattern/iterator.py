class MyDictIterator(object):
    def __init__(self, mydict):
        self.mylist = list(mydict.values())
        self.n = -1

    def __next__(self):
        if self.n == len(self.mylist) - 1:
            raise StopIteration
        else:
            self.n+=1
            return self.mylist[self.n]

class MySetIterator(object):
    def __init__(self, myset):
        self.mylist = list(myset)
        self.n = -1
    def __next__(self):
        if self.n == len(self.mylist) - 1:
            raise StopIteration
        else:
            self.n+=1
            return self.mylist[self.n]