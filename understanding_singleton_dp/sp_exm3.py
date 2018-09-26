class BaseConnection(object):
    INSTANCE = None
    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE is None:
            cls.INSTANCE = super(BaseConnection, cls).__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    def printConnection(self):
        print("This is base connection")

class SQLConnection(BaseConnection):
    def printConnection(self):
        print("This is SQL Connection")

class MongoConnection(BaseConnection):
    def printConnection(self):
        print("This is Mongo Connection")

if __name__ == '__main__':
    s1 = SQLConnection()
    s2 = MongoConnection()
    print(id(s1))
    print(id(s2))
    s1.printConnection()
    s2.printConnection()

    # We did not get a single object. We got multiple objects, which is what we may not want.
    # However, now if you create more connections of those types, it will always be the same
    s3 = SQLConnection()
    s4 = MongoConnection()
    print(id(s3))
    print(id(s4))
    s3.printConnection()
    s4.printConnection()

    print(s1 is s3)
    print(s2 is s4)