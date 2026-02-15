import uuid
import datetime as dt

class Member:
    """
    IN class behtarin class jahan ast
    RETURN: Member object
    Example:
    Member("John Doe")
    """
    def __init__(self, name, banned=False):
        self.name = name
        self.member_id = str(uuid.uuid4())
        self.rented_books = {}
        self.expiration_date = dt.datetime.now() + dt.timedelta(seconds=15)
        self.is_banned = banned
    
    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}"
    
    def list_rented_books(self):
        if not self.rented_books:
            print("Not rented books yet.")
            return
        print("List of rented books:")
        for book in self.rented_books.values():
            print(f"Book ID:{book.book_id}, Rented on:{book.rented_at}")
