#!/usr/bin/env python3
languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

if (len(languages) == 0):
    print("Dictionary is empty.")
for x in languages:
    print("{} was created by {}".format(x, languages[x]))
