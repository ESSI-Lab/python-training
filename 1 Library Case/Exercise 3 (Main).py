import m3module as m3m
import m3storage as m3s

book_list = m3s.load_books()

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
                while True:
                    title = input(f"Enter book title {i}: ").strip()
                    if title:
                        m3m.add_book(book_list, title)
                        break
                    else:
                        print("Try again, please input the title.")
            print("All book(s) added.")
        except ValueError:
            print("Please enter a valid number.")

    elif option == "2":
        title = input("Enter the book title to remove: ")
        m3m.remove_book(book_list, title)

    elif option == "3":
        print(m3m.show_books(book_list))

    elif option == "4":
        print(f"You have {m3m.count_books(book_list)} book(s).")

    elif option == "5":
        sorted_books = m3m.sort_books(book_list)
        print(sorted_books)

    elif option == "6":
        keyword = input("Enter the search keyword: ")
        print(m3m.search_book(book_list, keyword))

    elif option == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option, please try again.")
