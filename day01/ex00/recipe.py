""" Recipe class

"""
import sys


def valid_values(name, lvl, time, ingr, desc, rtype):
    """A function that checks if the values are valid Recipe attributes"""
    valid = 1
    if not isinstance(name, str):
        print("Error : Name isn't a string.")
        valid = 0
    try:
        if len(name) == 0:
            print("Error : Name is empty.")
            valid = 0
    except TypeError:
        pass
    if not isinstance(lvl, int):
        print("Error : Cooking level isn't an integer.")
        valid = 0
    try:
        if not 0 < lvl < 6:
            print("Error : Cooking level value is invalid.")
            valid = 0
    except TypeError:
        pass
    if not isinstance(time, int):
        print("Error : Prep time isn't an integer.")
        valid = 0
    try:
        if time <= 0:
            print("Error : Prep time value is invalid.")
            valid = 0
    except TypeError:
        pass
    if not isinstance(ingr, list):
        print("Error : Ingredients isn't a list.")
        valid = 0
    try:
        if len(ingr) == 0:
            print("Error : Ingredient list is empty.")
            valid = 0
    except TypeError:
        pass
    if not isinstance(desc, str):
        print("Error : Description isn't a string.")
        valid = 0
    if not isinstance(rtype, str):
        print("Error : Recipe type isn't a string.")
        valid = 0
    try:
        if len(rtype) == 0:
            print("Error : Recipe type is empty.")
            valid = 0
    except TypeError:
        pass
    if rtype not in ('starter', 'lunch', 'dessert'):
        print("Error : Recipe type isn't starter, lunch or dessert.")
        valid = 0
    return valid


class Recipe:
    """A class to represent a recipe"""

    def __init__(self, name, lvl, time, ingr, desc, rtype):
        if valid_values(name, lvl, time, ingr, desc, rtype):
            self.name = name
            self.cooking_lvl = lvl
            self.cooking_time = time
            self.ingredients = ingr
            self.description = desc
            self.recipe_type = rtype
        else:
            sys.exit()

    def __str__(self):
        txt = ("Recipe : " + self.name + "\n"
               + "Cooking level : " + str(self.cooking_lvl) + "\n"
               + "Prep time : " + str(self.cooking_time) + " minutes\n"
               + "Ingredients : " + ', '.join(self.ingredients) + "\n"
               + "Description : " + self.description + "\n"
               + "Recipe type : " + self.recipe_type)
        return txt
