import datetime as dt

__author__ = "Nilofar Jafari"
__version__ = "1.0.0"
__email__ = "nilofar.jafari@gmail.com"
__status__ = "Development"

class StorageSystem:
    """IN class behtarin class jahan ast"""
    def __init__(self):
        self._books = []
        self._members = {}

    def get_members(self):
        """
        IN method behtarin method jahan ast
        RETURN: dictionary of members
        
        Example:
        {
            "1234567890": Member("John Doe"),
            "1234567891": Member("Jane Doe")
        }
        """
        return self._members

    def print_members(self, members_dict):
        print("List of members:")
        for member_id, member in members_dict.items():
            print(f"Member ID: {member_id}, Name: {member.name}, Expiration Date: {member.expiration_date}, Is Banned: {member.is_banned}")
        print(f"Total members: {len(members_dict)}")

    def get_non_expired_members(self):
        result = {}
        for member_id, member in self.get_members().items():
            if member.expiration_date > dt.datetime.now() and not member.is_banned:
                result[member_id] = member
        return result
    # setters and getters
    def get_books(self):
        return self._books

    def get_non_deleted_books(self):
        return [book for book in self._books if not book.is_delete]

    def add_book(self, book):
        self._books.append(book)
        print(f"Book added.\n {book}, Total books: {len(self._books)}")

    def list_books(self):
        for book in self.get_non_deleted_books():
            print(book)

    def search_book_by_title(self, title):
        result = []
        print(f"Searching title: {title}")
        found = False
        for book in self.get_non_deleted_books():
            if title.lower() in book.title.lower() :
                result.append(book)
                print(book)
                found = True
        if not found:
            print(f"No results.")
        return result
        
    def search_book_by_book_id(self, book_id):
        for idx, book in enumerate(self.get_non_deleted_books()):
            if book.book_id == book_id:
                return idx
        return None
    
    def search_book_by_language(self, language):
        result = []
        print(f"Searching language: {language}")
        for book in self.get_non_deleted_books():
            if book.language.lower() == language.lower():
                result.append(book)
                print(book)
        if not result:
            print(f"No results.")
        return result

    def search_book_by_category(self, category):
        result = []
        print(f"Searching category: {category}")
        for book in self.get_non_deleted_books():
            if category.lower() in book.category.lower():
                result.append(book)
                print(book)
        if not result:
            print(f"No results.")

    def remove_book_by_book_id(self, book_id):
        idx = self.search_book_by_book_id(book_id)
        if idx is None:
            print(f"Book id not found.")
            return
        self.books[idx].is_delete = True
        print(f"Book removed. {book_id}")

    def register_member(self, member):
        if member.member_id in self.get_members():
            print(f"Member already registered.")
            return
        else:  
            self._members[member.member_id] = member
            print(f"Registration successful. Name: {member.name}, Member ID: {member.member_id}")

    def rent_book_by_book_id(self,book_id, member_id):
        if member_id not in self.get_non_expired_members():
            print("Member not registered.")
            return
        idx = self.search_book_by_book_id(book_id)
        if idx is None:
            print(f"Book id not found.")
            return 
        if not self.books[idx].is_available: ##qustion
            print(f"Book unavailable.{book_id}")
            return
        if len(self.get_members()[member_id].rented_books) >= 2 :
            print("Rental limit reached(max 2 books).")
            return
        self.books[idx].is_available = False
        self.books[idx].rented_by = member_id
        self.books[idx].rented_at = dt.datetime.now().strftime("%Y-%B-%d  %H:%M")
        self._[member_id].rented_books[book_id] = self.books[idx]
        print(f"Book rented. Book ID: {book_id}  Member ID: {member_id}")

    def check_book_availablility(self,book_id):
        idx = self.search_book_by_book_id(book_id)    
        if idx is None:
            print("Book id not found.")
            return
        if not self.books[idx].is_available or self.books[idx].is_delete:
            print(f"Book unavailable.{book_id}")
            return
        print(f"Book available. {book_id}")

    def return_book(self, book_id):
        idx = self.search_book_by_book_id(book_id)
        if idx is not None:
            self.books[idx].is_available = True
            self.books[idx].return_at = dt.datetime.now().strftime("%Y-%m-%d  %H:%M")
            self._members[self.books[idx].rented_by].rented_books.pop(book_id)
            print(f"Book returned.")
            self.books[idx].rented_by = None
            self.books[idx].rented_at = None
            return
        print("Book id not found!")
    
    def modify_book_details(self,book_id, title=None, author=None, year=None, category=None, language=None):
        idx = self.search_book_by_book_id(book_id)
        if idx is None:
            print(f"Book id not found.")
            return
        if self.books[idx].is_delete:
            print("Cannot modify removed book.")
            return
        if title is not None:
            self.books[idx].title = title
        if author is not None:
            self.books[idx].author = author
        if category is not None:
            self.books[idx].category = category
        if language is not None:
            self.books[idx].language = language
            print("Book updated.")

    def update_member(self, member_id, name=None):
        if member_id not in self.get_members():
            print("Member not found.")
            return
        if name is not None:
            self._members[member_id].name = name
            print("Member updated.")
