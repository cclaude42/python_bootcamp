#!/usr/bin/env python3
from vector import Vector

v1 = Vector([0, 13.0, -2, 3.0])
print(v1)
v5 = v1 + 4
print(v5)
print()

v2 = Vector([[12.0], [24.0], [48.0]])
print(v2)
v6 = v2 - 1
print(v6)
print()

v3 = Vector(5)
print(v3)
v7 = v3 * 2
print(v7)
print()

v4 = Vector((10, 15))
print(v4)
v8 = v4 / 2
print(v8)
print()

# v9 = Vector([[1, 2], [8]]) # Invalid init

# v10 = 1 / v1 # Can't divide by vector

# v11 = "abc" + v3 # Invalid type for add

# v12 = v3 * v2 # Different sizes, invalid operation