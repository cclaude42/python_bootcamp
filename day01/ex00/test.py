from recipe import Recipe
from book import Book


listy = ['Pate', 'Saumon', 'Epinard']
tourte = Recipe("Tourte", 3, 15, listy, "", "lunch")
listy = ['Suce', 'Tes', 'Morts']
ton_pere = Recipe("Ton Pere", 3, 40, listy, "Ton pere le singe", "dessert")

first_book = Book("First book")
Book.add_recipe(first_book, tourte)
Book.add_recipe(first_book, 6)

Book.get_recipes_by_types(first_book, 'dessert')
