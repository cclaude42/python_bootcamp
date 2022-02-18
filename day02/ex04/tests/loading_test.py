#!/usr/bin/env python3
"""A file to test the loading bar package
"""
import time
from random import randint
from my_minipack.progressbar import progressbar

if __name__ == "__main__":
    listy = range(1001)
    ret = 0
    for elem in progressbar(listy):
        ret += (elem + 3) % 5
        time.sleep(0.005)
    print()
    print(ret)
