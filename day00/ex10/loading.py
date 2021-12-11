#!/usr/bin/env python3
import time
import sys


def ft_progress(list):
    start = time.time()
    mval = max(list)
    length = len(str(max(list)))
    eta = 0
    barsize = 40
    for i in list:
        per = i/mval*100
        bar = int(i/mval*barsize)
        t = time.time() - start
        if not per == 0:
            eta = t/per*100
        sys.stdout.write('\r')
        sys.stdout.write("ETA: %.2fs [%3d%%] [%-*.*s] %*d/%d | elapsed time %.2fs" % (eta, per, barsize, barsize, '='*bar+'>', length, i, mval, t))
        sys.stdout.flush()
        yield i

if __name__ == "__main__":
    listy = range(1001)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.005)
    print()
    print(ret)
