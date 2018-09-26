from understanding_facade_pattern import color
from understanding_facade_pattern import shape


class ColorShapeFacade(object):
    def __init__(self,r,b,s,c):
        self.r = r
        self.b = b
        self.s = s
        self.c = c

    def rc(self):
        self.c.draw()
        self.r.fill()
    def rs(self):
        self.s.draw()
        self.r.fill()
    def bc(self):
        self.c.draw()
        self.b.fill()
    def bs(self):
        self.s.draw()
        self.b.fill()

if __name__ == '__main__':
    csf = ColorShapeFacade(color.Red(), color.Blue(), shape.Square(), shape.Circle())
    csf.rc()
    csf.bs()
    csf.rs()
    csf.bc()
