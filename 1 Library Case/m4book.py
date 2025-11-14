class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def description(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages and costs ${self.price})"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "price": self.price
        }

    def from_dict(data):
        return Book(
            title=data["title"],
            author=data["author"],
            pages=data["pages"],
            price=data["price"]
        )
