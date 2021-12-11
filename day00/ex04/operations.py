#!/usr/bin/env python3
import sys


def is_int(s):
    i = len(s) - 1
    while (i >= 1):
        if not(s[i] >= '0' and s[i] <= '9'):
            return (0)
        i -= 1
    if not (s[0] == '-' or (s[i] >= '0' and s[i] <= '9')):
        return (0)
    if (s[0] == '-' and len(s) == 1):
        return (0)
    return (1)


if (len(sys.argv) == 3 and is_int(sys.argv[1]) and is_int(sys.argv[2])):
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum:          {}".format(a + b))
    print("Difference:   {}".format(a - b))
    print("Product:      {}".format(a * b))
    if (b == 0):
        print("Quotient:     ERROR (div by zero)")
        print("Remainder:    ERROR (modulo by zero)")
    else:
        print("Quotient:     {}".format(a / b))
        print("Remainder:    {}".format(a % b))
else:
    if (len(sys.argv) == 2):
        print("InputError: too few arguments")
    if (len(sys.argv) > 3):
        print("InputError: too many arguments")
    if (len(sys.argv) > 1 and is_int(sys.argv[1]) == 0):
        print("InputError: first argument invalid")
    if (len(sys.argv) > 2 and is_int(sys.argv[2]) == 0):
        print("InputError: second argument invalid")
    print("Usage: python operations.py")
    print("Example:\fpython operations.py 10 3")
