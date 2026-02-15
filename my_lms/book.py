import uuid

class Book:
    def __init__(self,title,author,year,category,language):
        self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.language = language
        self.rented_by = None
        self.rented_at = None
        self.return_at = None
        self.is_available = True
        self.is_delete = False

    def __str__(self):
        return f"Title: {self.title}, Book ID: {self.book_id}, Author: {self.author}, Year: {self.year}, Category: {self.category}, Language: {self.language}"