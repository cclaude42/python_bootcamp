""" Vector class

"""
def is_float_list(lst):
    """Tests whether object is list of floats or ints"""
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not isinstance(elem, int) and not isinstance(elem, float):
            return False
    return True

def is_list_list(lst):
    """Tests whether object is list of sublists of floats or ints"""
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not is_float_list(elem):
            return False
    return True

def is_rectangular(lst):
    """Tests whether object is list with sublists of same size"""
    if not is_list_list(lst):
        return False
    size = len(lst[0])
    for elem in lst:
        if len(elem) != size:
            return False
    return True

def is_range(tpl):
    """Tests whether object is tuple that describes a range"""
    if not isinstance(tpl, tuple) or len(tpl) != 2:
        return False
    if isinstance(tpl[0], int) and isinstance(tpl[1], int) and tpl[0] < tpl[1]:
        return True
    return False

class Vector:
    """Mathematical class simulating a matrix"""

    def __init__(self, values):
        self.values = []
        if isinstance(values, list):
            if is_float_list(values):
                self.shape = (1, len(values))
                self.values.append(values.copy())
            elif is_list_list(values) and is_rectangular(values):
                self.shape = (len(values), len(values[0]))
                for elem in values:
                    self.values.append(elem.copy())
            else:
                raise ValueError("Invalid list for Vector")
        elif isinstance(values, int):
            self.shape = (values, 1)
            for i in range(values):
                self.values.append([float(i)])
        elif is_range(values):
            self.shape = (values[1] - values[0], 1)
            for i in range(values[0], values[1]):
                self.values.append([float(i)])
        else:
            raise ValueError("Invalid values for Vector")

    def __add__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, Vector) and self.shape == oper.shape:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.values[i][j] += oper.values[i][j]
        else:
            raise ValueError("Invalid type for addition")
        return new

    def __radd__(self, oper):
        return self.__add__(oper)

    def __sub__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, Vector) and self.shape == oper.shape:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.values[i][j] -= oper.values[i][j]
        else:
            raise ValueError("Invalid type for substraction")
        return new

    def __rsub__(self, oper):
        return self.__sub__(oper)

    def __truediv__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int) or isinstance(oper, float):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.values[i][j] /= oper
        else:
            raise ValueError("Invalid type for division")
        return new

    def __rtruediv__(self, oper):
        raise ValueError("Can't divide by Vector")

    def __mul__(self, oper):
        new = Vector(self.values)
        if isinstance(oper, int) or isinstance(oper, float):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new.values[i][j] *= oper
        else:
            raise ValueError("Invalid type for multiplication")
        return new

    def __rmul__(self, oper):
        return self.__mul__(oper)

    def __str__(self):
        txt = ("Vector values : " + str(self.values)
               + "\nShape : " + str(self.shape))
        return txt

    def __repr__(self):
        txt = str(self.values) + " : " + str(self.shape)
        return txt

    def dot(self, oper):
        """Returns the dot product of two vectors"""
        if self.shape[1] != oper.shape[0]:
            raise ValueError("Dot product requires a.shape[1] == b.shape[0]")
        product = [[0] * oper.shape[1] for i in range(self.shape[0])]
        print(product)
        for i in range(self.shape[0]):
            for j in range(oper.shape[1]):
                for k in range(self.shape[1]):
                    product[i][j] += self.values[i][k] * oper.values[k][j]
        return Vector(product)

    def T(self):
        """Returns the transpose matrix of the vector"""
        values = [[0] * self.shape[0] for i in range(self.shape[1])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                values[j][i] = self.values[i][j]
        return Vector(values)
