import json
import os

def load_books(filename="books.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_books(book_list, filename="books.json"):
    with open(filename, "w") as f:
        json.dump(book_list, f, indent=4)
