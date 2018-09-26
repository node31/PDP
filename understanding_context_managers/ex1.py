class MyContextManager(object):
    def __init__(self):
        print("%s is initialized" % self.__class__.__name__)
    def __enter__(self):
        print("Enter Called")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit Called")