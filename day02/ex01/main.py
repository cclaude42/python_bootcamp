#!/usr/bin/env python3
""" Args and kwargs main

"""
def what_are_the_vars(*args, **kwargs):
    """A function that creates and returns an ObjectC, after making its variables args and kwargs"""
    obj = ObjectC()
    for i, item in enumerate(args):
        setattr(obj, f"var_{i}", item)
    # obj.__dict__.update(kwargs)
    for key, value in kwargs.items():
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
    return obj


class ObjectC(object): # pylint: disable=missing-class-docstring
    def __init__(self):
        pass

def doom_printer(obj): # pylint: disable=missing-function-docstring
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value)) # pylint: disable=consider-using-f-string
    print("end")

def main(): # pylint: disable=missing-function-docstring
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)

if __name__ == "__main__":
    main()
