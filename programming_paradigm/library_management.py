# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title                # Public attribute
        self.author = author              # Public attribute
        self._is_checked_out = False      # Private attribute

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   # Private list of Book objects

    def add_book(self, book):
        """Adds a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Marks a book as checked out if found and available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Marks a book as returned (available) if found."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Displays all books that are not checked out."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
