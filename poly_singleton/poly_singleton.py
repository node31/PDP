class PolySingleton(object):
    """
    A class which supports maximum number of instances of a particular thing
    """
    _MAX_INSTANCES = 3
    _INSTANCE_LIST = [None] * _MAX_INSTANCES
    _CURR_INSTANCE = -1
    def __new__(cls, *args, **kwargs):
        cls._CURR_INSTANCE+=1
        if cls._CURR_INSTANCE >= cls._MAX_INSTANCES:
            cls._CURR_INSTANCE = 0

        if cls._INSTANCE_LIST[cls._CURR_INSTANCE] is None:
            cls._INSTANCE_LIST[cls._CURR_INSTANCE] = super(PolySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._INSTANCE_LIST[cls._CURR_INSTANCE]

if __name__ == '__main__':
    p1 = PolySingleton()
    p2 = PolySingleton()
    p3 = PolySingleton()
    print(id(p1), id(p2), id(p3))
    p1.x1 = 10
    p2.x2 = 20
    p3.x3 = 30
    p4 = PolySingleton()
    p5 = PolySingleton()
    p6 = PolySingleton()
    print(id(p4), id(p5), id(p6))
    print(p4.__dict__)
    print(p5.__dict__)
    print(p6.__dict__)
