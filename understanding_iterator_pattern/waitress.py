from understanding_iterator_pattern.menu import DinnerMenu, LunchMenu, BreakfastMenu


class Waitress(object):
    def __init__(self):
        self.menus = []
    def addMenu(self, menu):
        self.menus.append(menu)
    def __iter__(self):
        return iter(self.menus)

if __name__ == '__main__':
    w = Waitress()
    w.addMenu(DinnerMenu("DM", "This is DM"))
    w.addMenu(LunchMenu("LM", "This is LM"))
    w.addMenu(BreakfastMenu("BM", "This is BM"))
    for menu in w:
        for menu_item in menu:
            print(menu_item)