"""A module that contains the Book class."""

class Book:
    """A class to represent a book.
        - Initialized with title, author, ISBN, and (optionally) availability which defaults to True.
    """
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} {'is' if self.available else 'is not'} available"

    def display_info(self):
        """Display information about the book."""
        pass

    def toggle_availability(self):
        """Toggle the availability of the book."""
        self.available = not self.available
