from my_lms.storage_system import StorageSystem
from my_lms.book import Book
from my_lms.member import Member
from time import sleep



library = StorageSystem()

print(library.get_non_expired_members())
print(library.get_non_deleted_books())

member1 = Member("Nilofar Jafari")
member2 = Member("Maryam Ahmadi", banned=True)
library.register_member(member1)
library.register_member(member2)
library.print_members(library.get_members())
library.print_members(library.get_non_expired_members())

sleep(20)
library.print_members(library.get_members())
library.print_members(library.get_non_expired_members())
# book1 = Book("Python Crash Course", "Eric Matthes", "2015", "Education", "English")
# library.add_book(book1)
# book2 = Book("Divan Hafez", "Hafez Shirazi", "14th Century", "Poetry", "Persian")
# library.add_book(book2)
# book3 = Book("One Houndred Years of Solitude", "Gabriel Garcia", "1967", "Fiction", "Spanish")
# library.add_book(book3)
# book4 = Book("Symphony of the Dead", "Abbas Maroufi", "1989", "Psychological", "Persian")
# library.add_book(book4)
# print("================================================")

# # library.search_book_by_title("on")
# # library.search_book_by_language("persian")
# # library.search_book_by_category("Education")
# print("================================================")

# library.remove_book_by_book_id(book1.book_id)
# library.check_book_availablility(book1.book_id)

# member1 = Member("Nilofar Jafari")
# library.register_member(member1)

# library.rent_book_by_book_id(book1.book_id, member1.member_id)

# print("================================================")

# member1.list_rented_books()
# # library.check_book_availablility(book2.book_id)

# print("================================================")
# library.rent_book_by_book_id(book1.book_id, member1.member_id)
# library.rent_book_by_book_id(book2.book_id, member1.member_id)
# library.rent_book_by_book_id(book3.book_id, member1.member_id)
# library.rent_book_by_book_id(book4.book_id, member1.member_id)

# member1.list_rented_books()
# library.check_book_availablility(book3.book_id)

# print("================================================")
# library.return_book(book3.book_id)
# member1.list_rented_books()
# library.check_book_availablility(book3.book_id)

# print("=================================================")
# library.modify_book_details(book4.book_id, title= "aaaaa")
# # library.list_books()

# library.update_member(member1.member_id, name="nnnnn")
