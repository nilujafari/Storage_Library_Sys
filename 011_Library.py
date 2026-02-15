# Library Management System (LMS)
# The Library Management System is designed to help 
# libraries manage their operations more efficiently. 
# This system will provide functionalities for adding, modifying, and deleting book to the library.
# Features
# add book
# remove book
# search book
# rent book
# book availability
# Try to understand the question and plan before implementation!


class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True
        self.id = None
        self.category = None # fiction, non-fiction, science, history, etc.
        self.rented_by = None # name of the person who rented the book
        self.rented_at = None # date and time of the rental
    
    def __str__(self):
        return f"Book: {self.title}  ,  Author: {self.author} , Year: {self.year}  , ID: {self.id}"
    

class Library_Manage_Sys:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        number_of_books = len(self.books)
        book.id = number_of_books + 1
        self.books.append(book)
        print(book)
        print(f"Total books in the library: {number_of_books + 1}")

    def search_book_by_title(self, title):
        result = []
        print(f"Searching for books with title containing: {title}")
        found = False
        for book in self.books:
            if title.lower() in book.title.lower() :
                result.append(book)
                print(book)
                found = True

        if not found:
            print("Sorry! No book in the library.")
        
    def search_book_by_id(self, id):
        for idx, book in enumerate(self.books):
            if book.id == id:
                return idx
        return None


    def remove_book(self, id):
        idx = self.search_book_by_id(id)
        if idx is not None:
            self.books.pop(idx)
            print(f"Book with ID {id} removed successfully.")
        else:
            print(f"Book with ID {id} not found.")

    
  
    def rent_book(self,title):
        for i in self.books:
            if i.title == title and i.available: True
            print(F"You can borrow : {i} book.")
            return
        else:
            print("Sorry")

    def book_availablility(self,title):
        for i in self.books:
            if i.title == title and i.available: True
            print(f"They are availbale book is : {self.books}")
            return
        else:
            print("Sorry, the book is unavailable")



library = Library_Manage_Sys()

book1 = Book("Python crash course", "Eric Matthes", "2015")
book2 = Book("Animal farm", "George Orwell", "1945")
book3 = Book("One houndred years of solitude", "gabriel", "1967")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(Book("Learn english", "Michell", "2000"))

library.remove_book(1)

library.search_book_by_title("on")

# library.rent_book("Learn english")

# library.book_availablility("Learn english")
