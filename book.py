class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def get_info(self):
        return f"{self.title} by {self.author} ({self.year})"
