class Punto():
    def __init__ (self,x=0, y=0):
            self.x = x
            self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError('No puede ser negativo')
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __str__(self):
        return '({}, {})'.format(self.x,self.y)
