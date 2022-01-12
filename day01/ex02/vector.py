import sys

def isFloatList(lst):
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not isinstance(elem, int) and not isinstance(elem, float):
            return False
    return True

def isListList(lst):
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not isFloatList(elem):
            return False
    return True

def isRectangular(lst):
    if not isListList(lst):
        return False
    size = lst[0]
    for elem in lst:
        if len(elem) != size:
            return False
    return True

def isRange(tpl):
    if not isinstance(tpl, tuple) or len(tpl) != 2:
        return False
    if isinstance(tpl[0], int) and isinstance(tpl[1], int) and tpl[0] < tpl[1]:
        return True
    return False

class Vector:

    def __init__(self, values):
        self.values = []
        x = 0
        y = 0
        if isinstance(values, list):
            if isFloatList(values):
                x = 1
                y = len(values)
                for elem in values:
                    self.values.append(elem)
            elif isListList(values) and isRectangular(values):
                x = len(values)
                y = len(values[0])
                for elem in values:
                    self.values.append(elem)
            else:
                raise ValueError("Invalid list for Vector")
        elif isinstance(values, int):
            x = values
            y = 1
            for n in range(values):
                self.values.append(float(n))
        elif isRange(values):
            x = values[1] - values[0]
            y = 1
            for n in range(values[0], values[1]):
                self.values.append(float(n))
        else:
            raise ValueError("Invalid values for Vector")
        self.shape = (x, y)

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