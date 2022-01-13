#!/usr/bin/env python3
""" Book and recipe tests

"""
from recipe import Recipe
from book import Book

# Create Recipe :
listy = ['Pate', 'Saumon', 'Epinard']
tourte = Recipe("Tourte", 3, 20, listy, "", "lunch")

# Create second Recipe :
listy = ['Miel', 'Banane', 'Yaourt']
smoothie = Recipe("Smoothie miel-banane", 3, 10, listy,
        "Un smoothie de yaourt au miel et à la banane", "dessert")

# Create Book :
first_book = Book("First book")

### Testing :
# Add Recipe to Book
first_book.add_recipe(tourte)
first_book.add_recipe(smoothie)

# Add invalid Recipe to Book :
# Book.add_recipe(first_book, 6)

# Find recipes in Book by type :
Book.get_recipes_by_types(first_book, 'lunch')
print("")

# Print recipe from Book :
print(smoothie)
