
import uuid
import datetime as dt

class Member:
    def __init__(self, name):
        self.name = name
        self.member_id = str(uuid.uuid4())
        self.rented_books = {}
    
    def str(self):
        return f"Name:{self.name}, Member_id:{self.member_id}"
    
    def list_rented_books(self):
        if not self.rented_books:
            print("You have not rented any books yet.")
            return
        print("You have rented the following books:")
        for book in self.rented_books:
            print(book)

class Book:
    def __init__(self,title,author,year,category,language):
        self.title = title
        self.author = author
        self.year = year
        self.id = None
        self.category = category
        self.language = language
        self.rented_by = None
        self.rented_at = None
        self.return_at = None
        self.available = True
    def __str__(self):
        return f"Book:{self.title}, Author:{self.author}, Year:{self.year}, Category:{self.category}, Language:{self.language}, ID:{self.id}"

class Library_Manage_Sys:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, book):
        book.id = str(uuid.uuid4())
        self.books.append(book)
        print(book)
        print(f"Book added successfully with ID: {book.id} and now we have {len(self.books)} books in the library.")

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
    
    def search_book_by_language(self, language):
        result = []
        print(f"Searching for books with language containing: {language}")
        for book in self.books:
            if book.language.lower() == language.lower():
                result.append(book)
                print(book)
        if not result:
            print(f"Sorry! No books found with the selected language.")

    def search_book_by_category(self, category):
        result = []
        print(f"Searching for books with title containing: {category}")
        for book in self.books:
            if category.lower() in book.category.lower():
                result.append(book)
                print(book)
        if not result:
            print(f"Sorry! No books found with this category.")

    def remove_book(self, id):
        idx = self.search_book_by_id(id)
        if idx is not None:
            self.books.pop(idx)
            print(f"Book with ID {id} removed successfully.")
        else:
            print(f"Book with ID {id} not found.")

    def regester_member(self, member):
        if member.member_id in self.members:
            print(f"Your member ID : {member.member_id}")
            return
        else:  
            self.members[member.member_id] = member
            print("You are registered successfully:")
            print(f"Name: {member.name} , Member ID: {member.member_id}")

    def rent_book(self,id,member_id):
        #scan_id = input("Please ascan your ID:")
        if member_id not in self.members:
            print("You should register firstly.")
            return
        idx = self.search_book_by_id(id)
        if idx is not None:
            self.books[idx].available = False
            self.books[idx].rented_by = member_id
            self.books[idx].rented_at = dt.datetime.now().strftime("%Y-%B-%d  %H:%M")
            self.members[member_id].rented_books[id] = self.books[idx]
            print(f"Book with ID {id} rented successfully.")
            return
        print("Sorry! Book not found!")

    def check_book_availablility(self,id):
        for book in self.books:
            if book.id == id and book.available:
                print(f"Book withe ID: {id} available.")
                return
        else:
            print(f"Sorry!Book withe ID: {id} unavailable or not found.")

    def return_book(self, book_id):
        idx = self.search_book_by_id(book_id)
        if idx is not None:
            self.books[idx].available = True
            self.books[idx].return_at = dt.datetime.now().strftime("%Y-%B-%d  %H:%M")
            print(f"Book with ID {book_id} => {self.books[idx].rented_by}")
            self.members[self.books[idx].rented_by].rented_books.pop(book_id)
            print(f"Book with ID {book_id} returned successfully.")
            
            self.books[idx].rented_by = None
            self.books[idx].rented_at = None
            return
        
        print("Sorry! Book not found!")





library = Library_Manage_Sys()

book1 = Book("Python Crash Course", "Eric Matthes", "2015", "Education", "English")
book2 = Book("Divan Hafez", "Hafez Shirazi", "14th Century", "Poetry", "Persian")
book3 = Book("One Houndred Years of Solitude", "Gabriel Garcia", "1967", "Fiction", "Spanish")
book4 = Book("Symphony of the Dead", "Abbas Maroufi", "1989", "Psychological", "Persian")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# library.search_book_by_title("on")
# library.search_book_by_language("persian")
# library.search_book_by_category("Psychological")

# library.remove_book(1)


member1 = Member("Nilofar Jafari")
# member2 = Member("Maryam Ahmadi")

print("================================================")
library.regester_member(member1)
member1.list_rented_books()
library.check_book_availablility(book2.id)
# library.regester_member(member2)
print("================================================")

library.rent_book(book2.id,member1.member_id)
member1.list_rented_books()
library.check_book_availablility(book2.id)

print("================================================")
library.return_book(book2.id)
member1.list_rented_books()
library.check_book_availablility(book2.id)


#print(f"Name:{member1.name}, Member_id:{member1.member_id}")