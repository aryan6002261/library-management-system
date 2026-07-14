from library import Library
from book import Book
from utils import start_menu

library = Library()

while True:
    start_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        library.add_book(Book(book_id, title, author))

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        book_id = input("Book ID: ")
        library.issue_book(book_id)

    elif choice == "4":
        book_id = input("Book ID: ")
        library.return_book(book_id)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")