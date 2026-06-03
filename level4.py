class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f'"{self.title}" — {self.author}, {self.year} р.')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Книгу "{book.title}" додано.')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Книгу "{title}" видалено.')
                return
        print(f'Книгу "{title}" не знайдено.')

    def show_all(self):
        if not self.books:
            print("Бібліотека порожня.")
            return
        print("Список книг:")
        for book in self.books:
            book.display()


library = Library()

library.add_book(Book("Кобзар", "Тарас Шевченко", 1840))
library.add_book(Book("Тіні забутих предків", "Михайло Коцюбинський", 1911))
library.add_book(Book("1984", "Джордж Орвелл", 1949))

library.show_all()

library.remove_book("1984")

library.show_all()