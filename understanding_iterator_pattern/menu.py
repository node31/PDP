from understanding_iterator_pattern.menu_item import MenuItem
from understanding_iterator_pattern.iterator import MyDictIterator, MySetIterator
class Menu(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class BreakfastMenu(Menu):
    def __init__(self, name, description):
        self.bm = []
        self.addItem(MenuItem("B1", 10, True))
        self.addItem(MenuItem("B2", 20, False))
        self.addItem(MenuItem("B3", 30, False))
        super(BreakfastMenu, self).__init__(name, description)

    def addItem(self, menu_item):
        self.bm.append(menu_item)

    def __iter__(self):
        # Simply returning the iterator of the list
        return iter(self.bm)

class LunchMenu(Menu):
    def __init__(self, name, description):
        self.lm = {}
        self.addItem(MenuItem("L1", 100, True))
        self.addItem(MenuItem("L2", 200, False))
        self.addItem(MenuItem("L3", 300, False))
        super(LunchMenu, self).__init__(name, description)

    def addItem(self, menu_item):
        self.lm[menu_item.name] = menu_item

    def __iter__(self):
        # We will be implementing according to pow_two.py and better_pow_two.py
        # Read these classes throughly to understand why such thing was done
        return MyDictIterator(self.lm)



class DinnerMenu(Menu):
    def __init__(self, name, description):
        self.dm = set()
        self.addItem(MenuItem("D1", 1000, True))
        self.addItem(MenuItem("D2", 2000, False))
        self.addItem(MenuItem("D3", 3000, False))
        super(DinnerMenu, self).__init__(name, description)

    def addItem(self, menu_item):
        self.dm.add(menu_item)

    def __iter__(self):
        return MySetIterator(self.dm)


