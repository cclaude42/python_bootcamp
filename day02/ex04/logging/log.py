import time
from random import randint


def log(func):
    def wrapper(*args, **kwargs):
        file = open("machine.log", "a+")
        exec = time.time()
        s = str(func).split()[1].split('.')[-1].replace('_', ' ').title()
        file.write("(cclaude) Running: {:30}".format(s))
        result = func(*args, **kwargs)
        exec = time.time() - exec
        if exec > 0.001:
            file.write("[ exec-time = %.3f s ]\n" % exec)
        else:
            file.write("[ exec-time = %.3f ms ]\n" % (exec*1000))
        file.close()
        return result
    return wrapper
