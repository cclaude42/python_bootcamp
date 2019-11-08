import sys


class Vector:

    def __init__(self, values):
        if isinstance(values, list):
            self.values = values
            self.length = len(values)
        elif isinstance(values, int):
            self.values = []
            for f in range(values):
                self.values.append(float(f))
            self.length = values
        elif isinstance(values, tuple):
            self.values = []
            self.length = 0
            for f in range(values[0], values[1]):
                self.values.append(float(f))
                self.length += 1

    def __add__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i] + oper
        elif isinstance(oper, Vector):
            for i in range(self.length):
                new.values[i] = self.values[i] + oper.values[i]
        return (new)

    def __radd__(self, oper):
        return (self.__add__(oper))

    def __sub__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i] - oper
        elif isinstance(oper, Vector):
            for i in range(self.length):
                new.values[i] = self.values[i] - oper.values[i]
        return (new)

    def __rsub__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i]*(-1) + oper
        elif isinstance(oper, Vector):
            for i in range(self.length):
                new.values[i] = self.values[i]*(-1) + oper.values[i]
        return (new)

    def __truediv__(self, oper):
        if oper == 0:
            print("Error : can't divide by 0")
        else:
            new = Vector(self.values)
            for i in range(self.length):
                new.values[i] = self.values[i] / oper
                return (new)

    def __rtruediv__(self, oper):
        return (self.__truediv__(oper))

    def __mul__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i] * oper
        elif isinstance(oper, Vector):
            for i in range(self.length):
                new.values[i] = self.values[i] * oper.values[i]
        return (new)

    def __rmul__(self, oper):
        return (self.__mul__(oper))

    def __str__(self):
        txt = ("Vector values : " + str(self.values)
               + "\nNumber of values : " + str(self.length))
        return txt

    def __repr__(self):
        txt = (str(self.values) + " : " + str(self.length))
        return txt


v1 = Vector((10, 15))
print(v1)
v3 = v1 / 4
print(repr(v3))
