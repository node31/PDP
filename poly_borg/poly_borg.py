class PolyBorg(object):
    _MAX_STATES = 3
    _STATE_LIST = [{'a':1}, {'b':2}, {'c':3}]
    _CURR_STATE = -1
    def __init__(self):
        PolyBorg._CURR_STATE = (PolyBorg._CURR_STATE + 1)%(PolyBorg._MAX_STATES)
        print(PolyBorg._CURR_STATE)
        print(PolyBorg._STATE_LIST)
        self.__dict__ = PolyBorg._STATE_LIST[PolyBorg._CURR_STATE]

if __name__ == '__main__':
    p1 = PolyBorg()
    p2 = PolyBorg()
    p3 = PolyBorg()
    print(id(p1), id(p2), id(p3))

    print(p1.__dict__)
    print(p2.__dict__)
    print(p3.__dict__)
    p1.x1 = 10
    p2.x2 = 20
    p3.x3 = 30
    p4 = PolyBorg()
    p5 = PolyBorg()
    p6 = PolyBorg()
    print(id(p4), id(p5), id(p6))
    print(p4.__dict__)
    print(p5.__dict__)
    print(p6.__dict__)