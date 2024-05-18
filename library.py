"""A module for the Library class."""

class Library:
    """A class to represent a library."""

    def __init__(self, city):
        self.books = []
        self.city = city

    def __str__(self) -> str:
        return f"{self.city} Library"

    def transfer_book(self, book, library):
        """Return a book to the library."""
        if book in self.books:
            self.books.remove(book)
            library.add_book(book)
            print(f"{book.title} has been transferred to {library}.")
            return True

        return False

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def return_book(self, book):
        """Return a book to the library."""
        for book in self.books:
            if not book.available:
                book.toggle_availability()
                print(f"{book.title} has been returned.")
                return True
            else:
                print(f"{book.title} is already available.")
                return False

    def checkout_book(self, book):
        """Checkout a book from the library."""
        for book in self.books:
            if book.available:
                book.toggle_availability()
                print(f"{book.title} has been checked out.")
                return True
            else:
                print(f"{book.title} is not available for checkout.")
                return False

    def remove_book(self, book):
        """Remove a book from the library."""
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Cannot remove {book.title}. Title not found.")

    def search_by_title(self, title):
        """Search for a book by title and return a list of matching books."""
        matching_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                matching_books.append(book)
        return matching_books

    def search_by_author(self, author):
        """Search for a book by author and return a list of matching books."""
        matching_books = []
        for book in self.books:
            if author.lower() in book.author.lower():
                matching_books.append(book)
        return matching_books

    def display_catalog(self):
        """Display the library catalog."""
        if len(self.books) == 0:
            print("The library catalog is empty.")
        else:
            print(f"\n\n{self.city} Library Catalog:")
            for book in self.books:
                print(book)
