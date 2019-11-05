t = (256, 234, 45, 4)

if (isinstance(t, tuple) and len(t) == 0):
    print("There are no numbers.")
elif (isinstance(t, int)):
    print("The number is: {}".format(t))
elif (len(t) > 1):
    s = "{}".format(t[0])
    i = 1
    while (i < len(t)):
        s = s + ", {}".format(t[i])
        i += 1
    print("The {} numbers are: {}".format(i, s))
