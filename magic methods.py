# magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author} with {self.num_pages} pages"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages

book1 = book("Python", author="Ankur", num_pages=100)
book2 = book("Harry Uncle", author="JK rollin", num_pages=5640)
book3 = book("Python", author="Ankur", num_pages=5000)

print(book3)
print(book1 == book3)
print(book1 > book2)
print(book3 + book2)

print('Python' in book3)