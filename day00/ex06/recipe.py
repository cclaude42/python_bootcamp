#!/usr/bin/env python3
import sys


def print_recipe(name):
    if name in cookbook.keys():
        print("Recipe for {}:".format(name))
        print("Ingredient list: {}".format(cookbook[name][0]))
        print("To be eaten for {}.".format(cookbook[name][1]))
        print("Takes {} minutes of cooking.".format(cookbook[name][2]))
    else:
        print("Invalid recipe name.")


def del_recipe(name):
    if name in cookbook.keys():
        del cookbook[name]
        print("Deleted {} recipe.".format(name))
    else:
        print("Invalid recipe name.")


def add_recipe(name, ingredients, meal, time):
    if name in cookbook.keys():
        print("'{}' already exists, overwriting...".format(name))
    cookbook[name] = (ingredients, meal, time)
    print("Added '{}' to cookbook.".format(name))


def print_all():
    for x in cookbook.keys():
        print_recipe(x)
        print()


cookbook = {'sandwich': (['ham', 'bread', 'cheese', 'tomatoes'],
            'lunch', '10'),
            'cake': (['flour', 'sugar', 'eggs'], 'dessert', '60'),
            'salad': (['avocado', 'arugula', 'tomatoes', 'spinach'],
                      'lunch', '15')}

choice = 0
while not choice == 5:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    print(">> ", end="")
    sys.stdout.flush()
    try:
        choice = int(sys.stdin.readline())
    except ValueError:
        choice = 0
    print("")
    if choice == 1:
        name = input("Enter the name of the recipe you'd like to add: ")
        ingredients = input("Enter the ingredients in the format "
                            "'bread,butter,jam...': ").split(',')
        meal = input("Enter the type of meal (lunch, dessert...): ")
        time = input("Enter the recipe's prep time, in minutes: ")
        add_recipe(name, ingredients, meal, time)
    elif choice == 2:
        name = input("Enter the name of the recipe you'd like to delete: ")
        del_recipe(name)
    elif choice == 3:
        name = input("Please enter the recipe's name to get its details: ")
        print_recipe(name)
    elif choice == 4:
        print_all()
    elif choice == 5:
        print("Cookbook closed.")
    else:
        print("This option does not exist.")
    print()
