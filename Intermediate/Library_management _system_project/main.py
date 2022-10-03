from datetime import datetime


class Library:
    dictionary_lend_read = {}

    def __init__(self, library_name, available_books):
        self.library_name = library_name
        self.available_books = available_books

    def display_books(self):   ##A function to display books available
        for book in self.available_books:
            i = self.available_books.index(book)
            print(f"Book number{i+1}-{book}")

    def lend_book(self):  ##A function to let user rent or read any book
        customer_name1 = input("What's your good name!!-")
        flag = True
        while flag:
            book_name = input("Which book do you want-")
            print("Let me check whether it is available in the database of our library")
            for book in self.available_books:
                if book == book_name:
                    print("Yes!! The book is available")
                    choice2 = input("Whether do you wanna rent the book or read it in the library it self-")
                    if choice2 == "Rent" or choice2 == "rent":
                        with open("rent_lend_books.txt", "a") as rent:
                            rent.write(f"{customer_name1} rented {book_name} at {datetime.now()} ")
                    elif choice2 == "Read" or choice2 == "read":
                        self.dictionary_lend_read[book_name] = [customer_name1]
                    print("Thank you for taking our service")
                    break
                else:
                    print("Sorry book not available")
            choice = input("Do you want any other book(y/n)-")
            if choice == "Y" or choice == "y":
                flag = True
            else:
                flag = False

    def add_book(self):  #A function to let user donate any book to library
        customer_name2 = input("What's your good name!!-")
        donate_book_name = input("Which book do you want to donate-")
        self.available_books.append(donate_book_name)
        with open("donated_books.txt", "a") as don:
            don.write(f"{customer_name2} donated {donate_book_name} at {datetime.now()} ")
        print("Thank you for your donation,Task successfully completed")

    def return_book(self):    #A function to let user return book rented
        customer_name3 = input("What's your good name!!-")
        return_book_name = input("Which book do you want to return-")
        for key, value in self.dictionary_lend_read.items():
            if key == return_book_name:
                self.available_books.append(return_book_name)
                with open("returned_books.txt", "a") as ret:
                    ret.write(f"{customer_name3} returned {return_book_name} at {datetime.now()} ")
                break
        print("Thank you task successfully completed")

    def display_dictionary_lend_read(self):   #function for library staff to see who has taken which book
        print("\t\tWelCOME!!!\t\t")
        return self.dictionary_lend_read

    @staticmethod
    def rent_book_file():   #function for library staff to see records of books rented by the user
        with open("rent_lend_books.txt") as rent:
            for rented_books in rent:
                print(rented_books.rstrip())
        return "Finished"

    @staticmethod
    def add_book_file():    #function for library staff to see records of books donated by the user
        with open("donated_books.txt") as don:
            for donated_books in don:
                print(donated_books.rstrip())
        return "Finished"

    @staticmethod
    def ret_book_file():    #function for library staff to see records of books returned along with date by the user
        with open("returned_books.txt") as ret:
            for ret_books in ret:
                print(ret_books.rstrip())
        return "Finished"


if __name__ == '__main__':
    no_of_books = []

    def number_books(n):
        for i in range(n):
            no_of_books.append(input())
        print("Books added successfully")
    lib = Library("Bhavneet's Library", no_of_books)

    def manager():    #menu function for manager
        function = int(input("Enter what do you want to know\n1.Books taken to read\n2.Donation_file"
                             " \n3.Returned_books\n4.Books taken on rent\n5.Add any book"))
        if function == 1:
            lib.display_dictionary_lend_read()
        elif function == 2:
            lib.add_book_file()
        elif function == 3:
            lib.ret_book_file()
        elif function == 4:
            lib.rent_book_file()
        elif function == 5:
            n = int(input("How many book you want to enter"))
            number_books(n)

    def customer():   #menu function for customer
        function = int(input("Enter what do you want to do\n1.To see book available\n2.Rent or read any book"
                             "\n3.Donate any book\n4.Return any book-"))
        if function == 1:
            lib.display_books()
        elif function == 2:
            lib.lend_book()
        elif function == 3:
            lib.add_book()
        elif function == 4:
            lib.return_book()

    while True:
        print("\t\tWELCOME TO THE LIBRARY\t\t")
        role = int(input("Can you please tell your designation\n1.Manager\n2.Customer-"))
        if role == 1:
            manager()
        if role == 2:
            customer()