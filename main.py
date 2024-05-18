from dataset import books_data
from book import Book
from library import Library

# Create instance of Library class for the Lexington Library
lexington_library = Library("Lexington")

# Add all books to the Lexington Library
for book in books_data:
    # Create instance of Book class for each book in books_data
    book_instance = Book(book["title"], book["author"], book["isbn"], book["available"])
    lexington_library.add_book(book_instance)

# Display the catalog of the Lexington Library
# lexington_library.display_catalog()

# Create instance of Library class for the Louisville Library
louisville_library = Library("Louisville")

# Find 5 books by title and transfer them to the Louisville Library
books_by_title = lexington_library.search_by_title("of")
for book in books_by_title[:5]:
    if book.available:
        lexington_library.transfer_book(book, louisville_library)

# Display the catalog of the Lexington Library
lexington_library.display_catalog()

# Display the catalog of the Louisville Library
louisville_library.display_catalog()
