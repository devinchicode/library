class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

    def book_details(self):
        return f"book title is: {self.title}, the author is: {self.author}. Available: {self.is_available}"


class Member:
    def __init__(self, name: str, passport_id: int):
        self.name = name
        self.id = passport_id
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)
        book.is_available = False

    def book_return(self, book):
        self.borrowed_books.remove(book)
        book.is_available = True

    def show_books(self):
        for book in self.borrowed_books:
            print(book)


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        return f"{book} added successfully to the book list."

    def remove_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            return f"{book} remove successfully from the list."
        return f"{book} isn't in the library."

    def lend_book(self, member, book):
        if book in self.book_list and book.is_available:
            member.borrow(book)
            return f"The book {book.title} borrowed successfully to {member.name}."
        elif not book.is_available:
            return "Sorry, the book is borrowed by someone else now."

        else:
            return "Sorry, we don't have this book in our library right now."

    def return_book(self, member, book):
        if book in member.borrowed_books:
            member.book_return(book)
            return f"The book {book.title} returned successfully by {member.name}"
        else:
            return "You don't have this book in your borrowed books."

    def all_books(self):
        for book in self.book_list:
            print(book)
