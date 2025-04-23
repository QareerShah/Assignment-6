class Book:
    total_books = 0  # Class variable to track the total number of books

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increase total_books by 1

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment total_books when a new book is added


# Creating books and incrementing the book count
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")


# Display the total number of books
print(f"Total books: {Book.total_books}")
