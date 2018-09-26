from understanding_composite_pattern.menu_component import BreakfastMenu, Menu, LunchMenu, DinnerMenu


class Waitress(object):
    def __init__(self, menu_component):
        self.mc = menu_component

    def print(self):
        self.mc.print()


if __name__ == '__main__':
    m = Menu("AM", "This is AM")
    m.add(BreakfastMenu())
    m.add(LunchMenu())
    m.add(DinnerMenu())
    w = Waitress(m)
    w.print()
