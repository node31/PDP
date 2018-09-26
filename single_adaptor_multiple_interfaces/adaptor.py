from single_adaptor_multiple_interfaces import chef, diswasher, ingredients, meal
class VendorAdaptor(meal.Meal):
    def __init__(self, c,d,i):
        if not isinstance(c, chef.Chef):
            raise Exception("Invalid Chef")
        if not isinstance(d, diswasher.Diswasher):
            raise Exception("Invalid Dishwasher")
        if not isinstance(i, ingredients.Ing):
            raise Exception("Invalid Ingredients Obtainer")
        self.c = c
        self.d = d
        self.i = i

    def getMeal(self):
        self.i.obtainIngredients()
        self.c.prepareFood()

    def cleanDishes(self):
        self.d.cleanDishes()

if __name__ == '__main__':
    v = VendorAdaptor(chef.ExpensiveChef(), diswasher.IFBDishwaser(), ingredients.Chotu())
    v.getMeal()
    v.cleanDishes()