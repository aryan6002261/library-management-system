import json
from book import Book

FILE_NAME = "books.json"

def save_books(books):
    data = []
    for book in books:
        data.append({
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "available": book.available
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_books():
    books = []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            for item in data:
                book = Book(
                    item["book_id"],
                    item["title"],
                    item["author"]
                )
                book.available = item["available"]
                books.append(book)

    except FileNotFoundError:
        pass

    return books