""" Book class

"""
import sys
from datetime import datetime
from recipe import Recipe


class Book:
    """A class to represent a cookbook"""

    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = self.last_update
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

    def __str__(self):
        txt = ("Recipe book's name : " + self.name + "\n"
               + "Last update : " + str(self.last_update) + "\n"
               + "Creation date : " + str(self.creation_date) + "\n"
               + "Starters : " + str(self.recipes_list['starter']) + "\n"
               + "Lunches : " + str(self.recipes_list['lunch']) + "\n"
               + "Desserts : " + str(self.recipes_list['dessert']))
        return txt

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name specified and returns the instance"""
        if isinstance(name, str):
            for lst in self.recipes_list.values():
                for elem in lst:
                    if elem.name == name:
                        print(elem)
                        return elem
            print("Couldn't find the recipe you were looking for.")
        else:
            print("Error : Name isn't a string.")
        sys.exit()

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if isinstance(recipe_type, str):
            if recipe_type in self.recipes_list:
                print("Recipes in " + recipe_type + " :")
                for elem in self.recipes_list[recipe_type]:
                    print(elem.name)
                return
            else:
                print("Error : Recipe type isn't starter, lunch or dessert.")
        else:
            print("Error : Recipe type isn't a string.")
            sys.exit()

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            if recipe.recipe_type in self.recipes_list:
                self.recipes_list[recipe.recipe_type].append(recipe)
                self.last_update = datetime.now()
            else:
                print("Error : Recipe type isn't starter, lunch or dessert.")
        else:
            print("Error : Recipe isn't an instance of the Recipe class.")
            sys.exit()

#
# first_book = Book("First book")
# Book.get_recipes_by_types(first_book, 'starter')

# print(first_book.name)
# print(first_book.last_update)
# print(first_book.creation_date)
# print(first_book.recipes_list)
