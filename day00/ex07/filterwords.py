import sys
import string


valid = 0
if (len(sys.argv) == 3):
    try:
        length = int(sys.argv[2])
        valid = 1
    except ValueError:
        print("Invalid length parameter.")
elif (len(sys.argv) < 3):
    print("Too few arguments.")
elif (len(sys.argv) > 3):
    print("Too many arguments.")
if (valid == 1):
    s = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    t = s.split(' ')
    i = 0
    while i < len(t):
        if (len(t[i]) <= length):
            t.pop(i)
        else:
            i += 1
    print(t)
