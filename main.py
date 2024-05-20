from book import Book
from library import Library
from dataset import books_data

# Create instance of Library class for the Lexington Library
lexington_library = Library('Lexington')
print(lexington_library)


# Add all books, as book instances, to the Lexington Library
for book_dict in books_data:
    book_instance = Book(book_dict['title'], book_dict['author'], book_dict['isbn'], book_dict['available'])
    lexington_library.add_book(book_instance)


# Create instance of Library class for the Louisville Library
louisville_library = Library("Louisville")


# Find 5 books by title and transfer them to the Louisville Library
of_books = lexington_library.search_by_title("of")
first_five_books = of_books[:5]

for book in first_five_books:
    lexington_library.transfer_book(book, louisville_library)


# Display the catalog of the Lexington Library
print("Lexington Library Catalog")
lexington_library.display_catalog()

# Display the catalog of the Louisville Library
print("\n\nLouisville Library Catalog")
louisville_library.display_catalog()
