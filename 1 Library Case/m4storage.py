import json
import os
from m4book import Book

class Storage:
    def __init__(self, filename="books.json"):
        self.filename = filename

    def load_books(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    return [Book.from_dict(d) for d in data]
            except (json.JSONDecodeError, OSError):
                print("Error reading the book file — starting with an empty list.")
                return []
        else:
            return []

    def save_books(self, book_list):
        try:
            with open(self.filename, "w") as f:
                json.dump([book.to_dict() for book in book_list], f, indent=4)
        except OSError:
            print("Error saving books to file.")