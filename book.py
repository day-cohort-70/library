"""A module that contains the Book class."""

class Book:
    """A class to represent a book."""
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {availability}"

    def display_info(self):
        """Display information about the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Availability: {'Available' if self.available else 'Not Available'}")

    def toggle_availability(self):
        """Toggle the availability of the book."""
        self.available = not self.available
