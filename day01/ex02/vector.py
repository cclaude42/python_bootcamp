import sys


class Vector:

    def __init__(self, flist):
        self.values = flist
        self.length = len(flist)

    def __add__(self, num):
        for i in range(self.length):
            self.values[i] = self.values[i] + num

    def __radd__(self, num):
        print(num)
        for i in range(self.length):
            print("here!")
            self.values[i] = self.values[i] + num

v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector([0.0])
print(v1.values)
print(v1.length)
(v2).__radd__(v1)
print(v1.values)
print(v1.length)
