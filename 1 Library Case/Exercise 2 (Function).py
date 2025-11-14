book_list = []

def add_book(book_list, title):
    book_list.append(title)
    pass

def remove_book(book_list, title):
    if title in book_list:
        book_list.remove(title)
        print(f"'{title}' has been removed.")
    else:
        print(f"'{title}' was not found in your list.")

def show_books(book_list):
    if not book_list:
        return "You have no books yet."
    return "Your books are: " + ", ".join(book_list)

def count_books(book_list):
    return len(book_list)

def sort_books(book_list):
    return sorted(book_list, key=str.lower)

def search_book(book_list, keyword):
    results = [book for book in book_list if keyword.lower() in book.lower()]
    if results:
        return "Books found: " + ", ".join(results)
    else:
        return "No books match your keyword."

while True:
    print("\nChoose between these options:")
    print("1. Add book")
    print("2. Remove book")
    print("3. Show book list")
    print("4. Number of books")
    print("5. Sorted list of books")
    print("6. Search books based on Keywords")
    print("7. Quit")
    option = input("\nWrite the option you want: ")

    if option == "1":
        try:
            n = int(input("How many book(s) do you want to add? "))
            for i in range(1, n+1):
                title = input(f"Enter book title {i}: ")
                add_book(book_list, title)
            print("All book(s) added.")
        except ValueError:
            print("Please enter a valid number.")

    elif option == "2":
        title = input("Enter the book title to remove: ")
        remove_book(book_list, title)

    elif option == "3":
        shows = show_books(book_list)
        print(shows)

    elif option == "4":
        counted = count_books(book_list)
        print(f"You have {counted} book(s)")

    elif option == "5":
        sorted = sort_books(book_list)
        print(sorted)

    elif option == "6":
        keyword = input("Enter the search keyword: ")
        print(search_book(book_list, keyword))

    elif option == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option, please try again.")


