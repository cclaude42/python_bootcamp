"""A progress bar generator

Part of the my_minipack package
"""
import time
import sys


def progressbar(lst):
    """A progress bar to display progress.
    To be used as a generator.
    """
    start = time.time()
    mval = max(lst)
    length = len(str(max(lst)))
    eta = 0
    barsize = 40
    for i in lst:
        per = i/mval*100
        bar = int(i/mval*barsize)
        t = time.time() - start
        if not per == 0:
            eta = t/per*100
        sys.stdout.write('\r')
        sys.stdout.write("ETA: %.2fs [%3d%%] [%-*.*s] %*d/%d | elapsed time %.2fs" % (eta, per, barsize, barsize, '='*bar+'>', length, i, mval, t))
        sys.stdout.flush()
        yield i
