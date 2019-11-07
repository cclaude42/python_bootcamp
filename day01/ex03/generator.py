from time import time


def generator(text, sep=" ", option=None):
    if option == None:
        listy = text.split(sep)
    elif option == "shuffle":
        listy = set(text.split(sep))
    elif option == "unique":
        listy = list(dict.fromkeys(text.split(sep)))
    elif option == "ordered":
        listy = sorted(text.split(sep))
    for item in listy:
        yield item

text = "Le Lorem Ipsum est simplement du faux texte."
for i in generator(text, option="shuffle"):
    print(i)
