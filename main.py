from classes import Library
from books_and_members import *

library = Library()
library.add_book(indiana_book)
library.add_book(linux_book)
library.add_book(stocks_book)
# library.all_books()
# library.remove_book(indiana_book)
# library.all_books()

print(library.lend_book(George, indiana_book))
print("-----------------------")
print(library.lend_book(Leonardo, indiana_book))
print("-----------------------")
print(library.return_book(George, indiana_book))
print("-----------------------")
print(library.lend_book(Leonardo, indiana_book))
print("-----------------------")
library.all_books()
print("-----------------------")
