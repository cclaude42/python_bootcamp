import sys


class Vector:

    def __init__(self, values):
        self.values = []
        self.length = 0
        if isinstance(values, list):
            for f in values:
                if isinstance(f, list) and len(f) == 1 and (isinstance(f[0], float) or isinstance(f[0], int)):
                    self.values.append(float(f[0]))
                    self.length += 1
                elif isinstance(f, float) or isinstance(f, int):
                    self.values.append(float(f))
                    self.length += 1
                else:
                    raise ValueError("Invalid element in list: " + str(f))
        elif isinstance(values, int):
            for f in range(values):
                self.values.append(float(f))
            self.length = values
        elif isinstance(values, tuple):
            for f in range(values[0], values[1]):
                self.values.append(float(f))
                self.length += 1
        else:
            raise ValueError("Invalid values for Vector")

    def __add__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i] + oper
        elif isinstance(oper, Vector) and oper.length == self.length:
            for i in range(self.length):
                new.values[i] = self.values[i] + oper.values[i]
        else:
            raise ValueError("Invalid type for add")
        return (new)

    def __radd__(self, oper):
        return (self.__add__(oper))

    def __sub__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i] - oper
        elif isinstance(oper, Vector) and oper.length == self.length:
            for i in range(self.length):
                new.values[i] = self.values[i] - oper.values[i]
        else:
            raise ValueError("Invalid type for sub")
        return (new)

    def __rsub__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i]*(-1) + oper
        elif isinstance(oper, Vector) and oper.length == self.length:
            for i in range(self.length):
                new.values[i] = self.values[i]*(-1) + oper.values[i]
        else:
            raise ValueError("Invalid type for sub")
        return (new)

    def __truediv__(self, oper):
        if isinstance(oper, int) and oper != 0:
            new = Vector(self.values)
            return ([i / oper for i in self.values])
        elif isinstance(oper, int) and oper == 0:
            raise ValueError("Can't divide by zero")
        else:
            raise ValueError("Invalid type for div")

    def __rtruediv__(self, oper):
        raise ValueError("Can't divide by Vector")

    def __mul__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int):
            for i in range(self.length):
                new.values[i] = self.values[i] * oper
        elif isinstance(oper, Vector) and oper.length == self.length:
            for i in range(self.length):
                new.values[i] = self.values[i] * oper.values[i]
        else:
            raise ValueError("Invalid type for mul")
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