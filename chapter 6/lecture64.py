# # library managemnt 
# class Library:
#     def __init__(self):
#         self.books = []
#         self.no_of_books = 0
#     def insert(self, book):
#         self.books.append(book)
#         print("Book added!!")
#         self.no_of_books+=1
#         print("books:-",self.books,"number of books:",self.no_of_books)
#         user1.input()
#     def brought(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             print("Done!!")
#             self.no_of_books -= 1
#         else:
#             print("Book not found!")
#         print("books:-",self.books,"number of books:",self.no_of_books)
#         user1.input()
#     def request(self,choice):
#         if (choice in (1,2)):
#             if choice == 2:
#                 book_name = input(str("Enter book name:"))
#                 user1.insert(book_name)
#             elif choice == 1:
#                 book_name = input(str("Enter book name:"))
#                 user1.brought(book_name)
#         else:
#             print("User Exited!!")
#     def input(self):        
#         choice = int(input("Want to issue book/ book depositex/ End request (1/2/3): "))
#         user1.request(choice)
# choice = int(input("Want to issue book/ book depositex/ End request (1/2/3): "))
# user1 = Library()
# user1.request(choice)
class Library:
    def __init__(self):
        self.books = []
    
    def insert(self, book):
        self.books.append(book)
        print(f"Book '{book}' added! Total books: {len(self.books)}")

    def borrow(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' issued. Total books: {len(self.books)}")
        else:
            print(f"Book '{book}' not found!")

    def display_books(self):
        print("Current books in library:", self.books)

def main():
    library = Library()
    while True:
        try:
            choice = int(input("\n1. Issue a book\n2. Deposit a book\n3. Exit\nChoose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            book_name = input("Enter book name to issue: ")
            library.borrow(book_name)
        elif choice == 2:
            book_name = input("Enter book name to deposit: ")
            library.insert(book_name)
        elif choice == 3:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice.")
        
        library.display_books()

if __name__ == "__main__":
    main()
