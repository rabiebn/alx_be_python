## Mastering Inheritance and Composition in Python

class Book:
    """Base Class"""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"

class EBook(Book):

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return super().__str__() + f", File Size: {self.file_size}KB"
    
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return super().__str__() + f", Page Count: {self.page_count}"

class Library():
    
    books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.__str__())