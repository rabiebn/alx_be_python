## 

class Book:

    _is_checked_out = False

    def __init__(self, title, author):
        self.author = author
        self.title = title

class Library:

    _books = []

    def __init__(self):
        pass

    def add_book(self, newBook):
        self._books.append(newBook)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title and not book._is_checked_out:
                book._is_checked_out = True
                break

    def return_book(self, title):
        for book in self._books:
            if title == book.title and book._is_checked_out:
                book._is_checked_out = False
                break

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")

## return_book(self)
