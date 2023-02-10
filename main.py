class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages


    def __str__(self):
        return f"{self.name}"


    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, pages = {self.pages}"


class Library:
    def __init__(self, books=[]):
        self.books = books


    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            book = self.books[-1]
            return self.books.index(book) + 1


    def get_index_by_book_id(self):
        if len(self.books) == 0:
            return 0

#что получает метод?


class AudioBook(Book):
    def __init__(self, duration: float):
        self.duration = duration


class PaperBook(Book):
    def super(self):
        return super().pages   #super - заменяет self при наследовании


book = PaperBook()
print(book.pages)


lib = Library(['a', 'b'])
print(lib.get_next_book_id())