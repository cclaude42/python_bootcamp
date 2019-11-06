from datetime import datetime


class Book:

    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = self.last_update
        self.recipes_list = {'starter': None, 'lunch': None, 'dessert': None}

    def get_recipe_by_name(self, name):
        print(name)
        pass


first_book = Book("First book")

get_recipe_by_name(tourte)
print(first_book.name)
print(first_book.last_update)
print(first_book.creation_date)
print(first_book.recipes_list)
