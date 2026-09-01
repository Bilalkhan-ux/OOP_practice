class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        self.__available = True

    @property
    def available(self):
        return self.__available
    @available.setter
    def available(self,b):
        self.__available = b

    def borrowBook(self):
        self.__available = False

    def returnBook(self):
        self.__available = True

    def __str__(self):
        return f"Title: {self.title} Author: {self.author} Price: {self.price} Available: {self.available}"
   

class Library:
    def __init__(self):
        self.books = []
    def addBook(self,book):
        self.books.append(book)

    def showBooks(self):
        for book in self.books:
            print(book)

    def findBook(self,title):
        while True:
            for book in self.books:
                if book.title == title:
                    return book
            print("Not found")
            title = input("Enter title again: ")

    def borrowBook(self,title):
        book = self.findBook(title)
        if book.available:
            book.borrowBook()
            print("Book borrowed")
            print("*************")
        else:
            print("Book not available")

    def returnBook(self,title):
        book = self.findBook(title)
        book.returnBook()

    
library = Library()
while True:
    choice = int(input("Choose an option: \n1. Add book\n2. Show books\n3. Borrow book\n4. Return book\n5. Exit\n"))
    match choice:
        case 1:
            title = input("Enter title: ")
            authorName = input("Enter author name: ")
            price = int(input("Enter price: "))
            book = Book(title,authorName,price)
            library.addBook(book)
            print("Book added successfully")
            print("*************")

        case 2:
            library.showBooks()

        case 3:
            title = input("Enter title: ")
            library.borrowBook(title)

        case 4:
            title = input("Enter title: ")
            library.returnBook(title)
            print("Book returned")
            print("*************")

        case 5:
            break

        case _:
            print("Choose valid option")



