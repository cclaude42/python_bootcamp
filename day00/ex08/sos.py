#!/usr/bin/env python3
import sys
import string


morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ' ': '/'}


def print_morse(str):
    if str.translate(str.maketrans('', '', ' ')).isalnum():
        str = str.upper()
        for c in str:
            print(morse_dict[c], end=" ")
        print("")
    else:
        print("Invalid characters in string given.")


if len(sys.argv) > 1:
    str = sys.argv[1]
    for i in range(len(sys.argv) - 2):
        str = str + " " + sys.argv[i + 2]
    print_morse(str)
else:
    print("Too few arguments.")
