#!/usr/bin/env python3
import sys


def not_int(s):
    i = len(s) - 1
    while (i >= 1):
        if not(s[i] >= '0' and s[i] <= '9'):
            return (1)
        i -= 1
    if not (s[0] == '-' or (s[i] >= '0' and s[i] <= '9')):
        return (1)
    if (s[0] == '-' and len(s) == 1):
        return (1)
    return (0)


if (len(sys.argv) != 2 or not_int(sys.argv[1])):
    print("ERROR")
else:
    if (int(sys.argv[1]) == 0):
        print("I'm Zero.")
    elif (int(sys.argv[1]) % 2 == 0):
        print("I'm Even.")
    elif (int(sys.argv[1]) % 2 == 1):
        print("I'm Odd.")
