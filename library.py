from book import Book
import os,csv

class Library:
    def __init__(self):
        self.books = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_dir, "books.csv")
        self.load_books()
        print("CSV path:", os.path.abspath(self.filename))

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()

    def show_books(self):
        for book in self.books:
            print(book.get_info())
    
    def save_books(self):
        with open(self.filename,"w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["title","author","year","available"])

            for book in self.books:
                writer.writerow([book.title,book.author,book.year,book.available])

    def load_books(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename,"r",encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                book = Book(row["title"],row["author"],int(row["year"]))
                self.books.append(book)
                if "available" in row:
                    book.available = row["available"] == "True"
                    

    
