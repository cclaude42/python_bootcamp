#!/usr/bin/env python3
phrase = "The right format"

if (len(phrase) <= 42):
    s = (42 - len(phrase)) * "-"
    print(s + phrase, end="")
else:
    print("Phrase is too long.")
