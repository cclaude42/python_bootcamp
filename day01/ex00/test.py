from recipe import Recipe
from book import Book

# Create Recipe :
listy = ['Pate', 'Saumon', 'Epinard']
tourte = Recipe("Tourte", 3, 15, listy, "", "lunch")

# Create second Recipe :
listy = ['Suce', 'Tes', 'Morts']
ton_pere = Recipe("Ton Pere", 3, 40, listy, "Ton pere le singe", "dessert")

# Create Book :
first_book = Book("First book")

### Testing :
# Add Recipe to Book
Book.add_recipe(first_book, tourte)

# Add invalid Recipe to Book :
# Book.add_recipe(first_book, 6)

# Find recipes in Book by type :
Book.get_recipes_by_types(first_book, 'lunch')
print("")

# Print recipe from Book :
print(tourte)
