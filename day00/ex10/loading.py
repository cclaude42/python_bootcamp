import time
import sys


def ft_progress(list):
    start = time.time()
    mval = max(list)
    length = len(str(max(list)))
    eta = 0
    for i in list:
        per = i/max(list)*100
        bar = int(i/max(list)*20)
        t = time.time() - start
        if not per == 0:
            eta = t/per*100
        sys.stdout.write('\r')
        sys.stdout.write("ETA: %.2fs [%3d%%] [%-20.20s] %*d/%d | elapsed time %.2fs" % (eta, per, '='*bar+'>', length, i, mval, t))
        sys.stdout.flush()
        yield i


listy = range(2000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
