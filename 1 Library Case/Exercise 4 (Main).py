import m4module as m4m
from m4book import Book
from m4storage import Storage

storage = Storage()
book_list = storage.load_books()

while True:
    print("\nChoose between these options:")
    print("1. Add book")
    print("2. Remove book")
    print("3. Show book list")
    print("4. Number of books")
    print("5. Sorted list of books")
    print("6. Search books based on Keywords")
    print("7. Save & quit")

    option = input("Write the option you want: ")

    if option == "1":
        try:
            n = int(input("How many book(s) do you want to add? "))
            for i in range(1, n + 1):
                print(f"\nWrite 'Book {i}' details:")
                while True:
                    title = input("Title: ").strip()
                    author = input("Author: ").strip()
                    pages = input("Total pages: ").strip()
                    price = input("Price: ").strip()

                    if not title or not author or not pages or not price:
                        print("Try again — all fields are required.")
                    else:
                        book = Book(title, author, pages, price)
                        m4m.add_book(book_list, book, storage)
                        break
        except ValueError:
            print("Please enter a valid number.")

    elif option == "2":
        print(m4m.show_books(book_list))
        title = input("Which Book would you like to remove? (write book number): ")
        m4m.remove_book(book_list, title)

    elif option == "3":
        print(m4m.show_books(book_list))

    elif option == "4":
        print(f"You have {m4m.count_books(book_list)} book(s).")

    elif option == "5":
        sorted_books = m4m.sort_books(book_list)
        print("\nSorted book list:")
        for i, book in enumerate(sorted_books, 1):
            print(f"{i}. {book.description()}")

    elif option == "6":
        keyword = input("Enter the search keyword: ")
        print(m4m.search_book(book_list, keyword))

    elif option == "7":
        storage.save_books(book_list)
        print("Books saved. Goodbye!")
        break

    else:
        print("Invalid option, please try again.")
