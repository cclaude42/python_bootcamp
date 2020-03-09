import sys

i = len(sys.argv)
while (i > 1):
    i -= 1
    s = sys.argv[i]
    j = len(s) - 1
    while (j >= 0):
        if (s[j] >= 'a' and s[j] <= 'z'):
            print(chr(ord(s[j]) - 32), end='')
        elif (s[j] >= 'A' and s[j] <= 'Z'):
            print(chr(ord(s[j]) + 32), end='')
        else:
            print(s[j], end='')
        j -= 1
    if (i > 1):
        print(' ', end='')
    else:
        print('')

# print(''.join([i.upper() if i.islower() else i.lower() for i in ''.join(sys.argv[1:])][::-1]))
