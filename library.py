from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.display()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                print("Book issued successfully.")
                return
        print("Book not available.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book returned successfully.")
                return