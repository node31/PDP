import abc


class MenuComponent(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def add(self, menu_component):
        raise NotImplementedError

    @abc.abstractmethod
    def print(self):
        raise NotImplementedError


class MenuItem(MenuComponent):
    def __init__(self, name, price, veg):
        self.price = price
        self.veg = veg
        super(MenuItem, self).__init__(name)

    def add(self, menu_component):
        raise NotImplementedError

    def print(self):
        print("[MenuItem: %s %s %s]" % (self.name, self.price, self.veg))


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.description = description
        self.mc_list = []  # This is a list which stores all MenuComponents
        super(Menu, self).__init__(name)

    def add(self, menu_component):
        self.mc_list.append(menu_component)

    def print(self):
        print("[%s %s %s]" % (self.__class__.__name__, self.name, self.description))
        for menu_component in self.mc_list:
            menu_component.print()


class BreakfastMenu(Menu):
    def __init__(self):
        super_obj = super(BreakfastMenu, self)
        super_obj.__init__("BM", "This is BM")
        super_obj.add(MenuItem("B1", 10, True))
        super_obj.add(MenuItem("B2", 20, False))
        super_obj.add(MenuItem("B3", 30, False))


class LunchMenu(Menu):
    def __init__(self):
        super_obj = super(LunchMenu, self)
        super_obj.__init__("LM", "This is LM")
        super_obj.add(MenuItem("L1", 100, True))
        super_obj.add(MenuItem("L2", 200, False))
        super_obj.add(MenuItem("L3", 300, False))


class DinnerMenu(Menu):
    def __init__(self):
        super_obj = super(DinnerMenu, self)
        super_obj.__init__("DM", "This is DM")
        super_obj.add(MenuItem("D1", 1000, True))
        super_obj.add(MenuItem("D2", 2000, False))
        super_obj.add(MenuItem("D3", 3000, False))
        super_obj.add(DessertMenu())


class DessertMenu(Menu):
    def __init__(self):
        super_obj = super(DessertMenu, self)
        super_obj.__init__("DesM", "This is DesM")
        super_obj.add(MenuItem("Des1", 1, True))
        super_obj.add(MenuItem("Des2", 2, True))

if __name__ == '__main__':
    print("HW")

