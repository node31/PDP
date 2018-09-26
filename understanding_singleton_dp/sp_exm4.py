class BaseConnection(object):
    INSTANCE = None
    def __new__(cls, *args, **kwargs):
        if cls.INSTANCE is None:
            cls.INSTANCE = super(BaseConnection, cls).__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    def printConnection(self):
        print("This is base connection")

class SQLConnection(BaseConnection):
    def __new__(cls, *args, **kwargs):
        return super(SQLConnection, cls).__new__(BaseConnection, *args, **kwargs)

    def printConnection(self):
        print("This is SQL Connection")

class MongoConnection(BaseConnection):
    def __new__(cls, *args, **kwargs):
        return super(MongoConnection, cls).__new__(BaseConnection, *args, **kwargs)

    def printConnection(self):
        print("This is Mongo Connection")

if __name__ == '__main__':
    s1 = SQLConnection()
    s2 = MongoConnection()
    print(id(s1))
    print(id(s2))
    s1.printConnection()
    s2.printConnection()
    # We got the exact same connection which we may not want.
