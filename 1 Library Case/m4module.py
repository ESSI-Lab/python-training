from m4storage import Storage
storage = Storage()

def add_book(book_list, book, storage):
    book_list.append(book)
    storage.save_books(book_list)
    print(f"'{book.title}' added successfully.")

def remove_book(book_list, identifier):
    if identifier.isdigit():
        index = int(identifier) - 1
        if 0 <= index < len(book_list):
            removed_book = book_list.pop(index)
            print(f"'{removed_book.title}' by {removed_book.author} has been removed.")
            return
        else:
            print("Invalid number. Please choose a valid book number.")
            return

def show_books(book_list):
    if not book_list:
        return "You have no books yet."
    result = "\nYour books:\n"
    for i, book in enumerate(book_list, start=1):
        result += f"Book {i}: {book.description()}\n"
    return result

def count_books(book_list):
    return len(book_list)

def sort_books(book_list):
    return sorted(book_list, key=lambda b: b.title.lower())

def search_book(book_list, keyword):
    keyword = keyword.lower().strip()
    results = [
        b for b in book_list
        if keyword in b.title.lower() or keyword in b.author.lower()
    ]
    if results:
        return "Books found:\n" + "\n".join(f"- {b.description()}" for b in results)
    else:
        return "No books match your keyword."