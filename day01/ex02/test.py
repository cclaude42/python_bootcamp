#!/usr/bin/env python3
""" Vector tests

"""
from vector import Vector

v1 = Vector([0, 13.0, -2, 3.0])
print(v1)
v5 = v1 * 4
print(v5)
print()

v2 = Vector([[12.0, 4], [24.0, 6], [48.0, 8]])
print(v2)
v6 = v2 / 2
print(v6)
print()

v3 = Vector(5)
print(v3)
v7 = v3 + Vector([[0], [10], [20], [30], [40]])
print(v7)
print()

v4 = Vector((10, 15))
print(v4)
v8 = v2 - Vector([[6.0, 4], [12, 6], [24.0, 8]])
print(v8)
print()

va = Vector([[1, 2, 3], [4, 5, 6]])
vb = Vector([[7, 8], [9, 10], [11, 12]])
vc = va.dot(vb)
print(vc)
print()

va = Vector([1, 10, 100])
vb = Vector([[1], [10], [100]])
vc = va.dot(vb)
print(vc)
print()

print(v2.T())

# v9 = Vector([[1, 2], [8]]) # Invalid init

# v10 = 1 / v1 # Can't divide by vector

# v11 = "abc" + v3 # Invalid type for add

# v12 = v3 * v2 # Different sizes, invalid operation
