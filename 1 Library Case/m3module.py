class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def description(self):
        return f"'{self.title}' by {self.author} — {self.pages} pages, costs ${self.price}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            pages=data["pages"],
            price=data["price"]
        )