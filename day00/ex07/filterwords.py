#!/usr/bin/env python3
import sys
import string


if (len(sys.argv) == 3):
    try:
        length = int(sys.argv[2])
    except ValueError:
        print("Invalid length parameter.")
        sys.exit()
elif (len(sys.argv) < 3):
    print("Too few arguments.")
    sys.exit()
elif (len(sys.argv) > 3):
    print("Too many arguments.")
    sys.exit()

s = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
t = s.split(' ')
i = 0
while i < len(t):
    if (len(t[i]) <= length):
        t.pop(i)
    else:
        i += 1
print(t)
