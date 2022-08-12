import random
import datetime


borrowed_books = []
clients_list = []
librarians_list = []
books_list = []
total_borrowed_books = []
avialable_books = []

class Client:
    def __init__(self, full_name , age, id_no, phone_no):
        self.id = random.randint(10000,99999)
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_no = phone_no

    def get_Client(self):
        print({"client id" : self.id,
                 "full_name" : self.full_name,
                 "age" : self.age,
                 "phone_no" : self.phone_no,
                 "id_no" : self.id_no
        })


class Librarian(Client):
    salary = 0.0
    def __init__(self, full_name, age, id_no, phone_number, salary):
        super().__init__(full_name, age, id_no, phone_number)
        self.salary = salary
#Create a method to change salary and to get librarian info
    def change_salary(self,new_salary):
        self.salary = new_salary
    def get_Librarian(self):
        return {
            "id" : self.id,
            "full_name" : self.full_name,
            "age" : self.age,
            "phone_no" : self.phone_no,
            "id_no" : self.id_no,
            "salary" : self.salary
        }

class Book:

    def __init__(self, title, description, author, status = "active"):
        self.id = random.randint(1, 1000)
        self.title = title
        self.description = description
        self.author = author
        self.status = status

    def get_id(self):
        return self.id

    def get_book(self):
        return {
            "Book id" : self.id,
            "Status" : self.status,
            "Title" : self.title,
            "Description" : self.description,
            "Author" : self.author
        }
    def get_book_status(self):
        return self.status

books_list.append(Book('The Universe In A Nutshell','Published in 1988,discusses of what was then known about the universe and '
      'the extraordinary advances in our understanding of the space and time','Stephen Hawking'))
books_list.append(Book('The Little Prince',"a young prince who visits various planets in space, including Earth, and addresses themes of loneliness, friendship, love, and loss.",
                  'Antoine de Saint-Exupéry'))
books_list.append(
    Book('The Kite Runner', 'Published in 2003, it tells the story of Amir, a young boy from the Wazir Akbar Khan district of Kabul'
         , 'Khaled Hosseini'))
books_list.append(Book('The Fault In our Stars', 'a fabulous book about a young girl diagnosed with lung cancer and attends a cancer support group.',
                      'John Green'))
books_list.append(Book('Returning To Haifa',
                  'One of Kanafanis most wonderful stories! It sheds some light on the events of Palestinian exodus',
                'Ghassan Kanafani'))

print(books_list)

class BorrowingBooks:

    def __init__(self, book_id, client_id, status = "Active"):
        days = int(input('how many days you want to borrow your book:'))
        self.start_date = datetime.date.today()
        self.end_date = datetime.date.today() + datetime.timedelta(days)
        self.book_id = book_id
        self.client_id = client_id
        self.status = status

    def get_id(self):
        return self.book_id

    def get_status(self):
        return self.status

    def update_status(self):
        if self.end_date >= self.start_date:
           status = "In Active-Not available"
           self.status

        else:
            self.status = "Active-Available"
            return self.status

    def get_orderInfo(self):
        return {
          'Book ID : ': self.book_id,
          "Client ID": self.client_id,
          "Status now ": self.status,
          'Start date ': self.start_date,
           "End date": self.end_date

        }

def add_client():

    full_name = input("enter your full name:")
    age = int(input("Enter Your Age"))
    phone_no = input("enter your Phone Number")
    id_no = input("Enter Your ID NO.")
    new_client = Client(full_name = full_name,age = age,phone_no = phone_no,id_no = id_no)
    clients_list.append(new_client)
    print("User has been succesfully added")
    print(new_client.get_Client())
    return(new_client)

def add_librarian():

    librarians_list.append(Librarian(str(input("full_name : ")), int(input(' age : ')), str(input('ID number : ')),
                                    int(input(' phone_no: ')), int(input('Salary : '))))
    print('Librarian has been added successfully')

def borrow_books():

    client_id = input('Enter Your client ID:')
    is_exist = False
    for i in clients_list:
        if i.id == client_id:
           is_exist = True
        for j in books_list:
            print(j.get_book())
        select_book = int(input('Enter the book you want to borrow:'))

        for t in range(0,len(books_list)):

            if select_book == ( books_list[t].get_id() ):
                print('chosen book: ', select_book)

                borrow = BorrowingBooks(select_book, client_id, status="In Active")
                borrowed_books.append(borrow)
                print('your borrowing order is created')
                print(borrow.get_orderInfo())
                del books_list[t]
                break
        break

        if not is_exist:
            print('please re-run the program and add client to the list')
            print(exit())



    for j in books_list:
        print("Available books to borrow:",
              j.get_book())

def return_book():
    returnBook = int(input('Enter your book id : '))
    for i in range (len(borrowed_books)):
        if returnBook == (borrowed_books[i].get_id()):
            books_list.append(borrowed_books[i])
        else:
            print('The id entered is not in the borrowed list, please try again')



while True:
    choice = int( input("1. Borrow book\n2. Add client\n3. Add librarian\n4. Return book\n5. Exit\nWhat do you want to do? :"))
    if choice == 1:
        borrow_books()

    elif choice == 2:
       add_client()

    elif choice == 3:
        add_librarian()

    elif choice == 4:
        return_book()

    elif choice == 5:
        exit()
