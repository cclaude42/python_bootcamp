#!/usr/bin/env python3
t = (3, 30, 2019, 9, 25)

m = ""
d = ""
y = ""
h = ""
min = ""
if (len(t) >= 5):
    if t[3] < 10:
        m = "0"
    if t[4] < 10:
        d = "0"
    if t[2] < 1000:
        y = "0"
    if t[2] < 100:
        y = "00"
    if t[2] < 10:
        y = "000"
    if t[0] < 10:
        h = "0"
    if t[1] < 10:
        min = "0"
    print("{}{}/{}{}/{}{} {}{}:{}{}"
          .format(m, t[3], d, t[4], y, t[2], h, t[0], min, t[1]))
else:
    print("Tuple needs at least five parameters.")
