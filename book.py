"""A module that contains the Book class."""

class Book:
    """A class to represent a book.
        - Initialized with title, author, ISBN, and (optionally) availability which defaults to True.
    """
    def __init__(self, title, author, isbn, available=True):
        pass

    def __str__(self):
        return "A Book"

    def display_info(self):
        """Display information about the book."""
        pass

    def toggle_availability(self):
        """Toggle the availability of the book."""
        pass
