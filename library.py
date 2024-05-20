"""A module for the Library class."""

class Library:
    """A class to represent a library. Initialized with city name."""

    def __init__(self, city_name):
        self.city_name = city_name
        self.books = []

    def __str__(self) -> str:
        return f"The {self.city_name} library"

    def transfer_book(self, book, library):
        """Transfer book to another library."""

        # Does this library have this book?
        if book in self.books:
            # Remove it from library A
            self.remove_book(book)

            # Add to library B
            library.add_book(book)

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def return_book(self, book):
        """Return a book to the library."""
        pass

    def checkout_book(self, book):
        """Checkout a book from the library."""
        pass

    def remove_book(self, book):
        """Remove a book from the library."""
        self.books.remove(book)

    def search_by_title(self, title):
        """Search for a book by title and return a list of matching books."""
        found_books = []
        for book in self.books:
            if title in book.title:
                found_books.append(book)

        return found_books


    def search_by_author(self, author):
        """Search for a book by author and return a list of matching books."""
        pass

    def display_catalog(self):
        """Display the library catalog."""
        for book in self.books:
            print(book)