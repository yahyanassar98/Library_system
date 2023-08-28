class Library:
    def __init__(self) -> None:
        self.members = []
        self.books = []

############# methods for member ########################

    def add_member(self):
        name = input('* Enter member name: ')
        email = input('* Enter member email: ')
        level = input('* Enter member level (A/B/C): ').upper()

        while True:
            if level in ['A', 'B', 'C']:
                member = Member(name, email, level)
                self.members.append(member)
                print('# Member added successfully')
                break
            else:
                level = input('Invalid Input ! , Please enter member level again (A/B/C): ').upper()


    def edit_member(self):
        id = int(input('* Enter member ID: '))
        for memb in self.members:
            if id == memb.id:
                name = input('* Enter new name: ')
                email = input('* Enter new email: ')
                level = input('* Enter member level (A/B/C): ').upper()
                while True:
                    if level in ['A', 'B', 'C']:
                        memb.name = name
                        memb.email = email
                        memb.level = level
                        print('# Member details updated successfully')
                        break
                    else:
                        level = input('Invalid Input ! , Please enter member level again (A/B/C): ').upper()
                break                        
        else:
            print('# Member ID NOT Found.')


    def show_members(self):
        space = ' ' * 30
        # max lenght of name is (15) and max length of email is (30)
        print(f'ID  | Name{" " * 11}| Email{" " * 25}| Level')
        print('-' * 65)

        for memb in self.members:
            s1 = 15 - len(memb.name)    # spaces after name
            s2 = 30 - len(memb.email)   # spaces after email
            print(f'{memb.id}   | {memb.name + space[:s1]}| {memb.email + space[:s2]}| {memb.level}')



    def delete_member(self):
        id = int(input('* Enter member ID: '))
        for memb in self.members:
            if id == memb.id:
                self.members.remove(memb)
                print(f'# Member {memb.name} deleted successfully')
                ### if user deleted then will return the status of his borrowed books into available
                for book in self.books:
                    if book.id in memb.borrowd:
                        book.status = False
                break
        else:
            print('# Member ID NOT Found.')


############# methods for book ########################

    def add_book(self):
        # self.members.append(member)
        title = input('* Enter book title: ')
        author = input('* Enter book author: ')
        level = input('* Enter book level (A/B/C): ').upper()

        while True:
            if level in ['A', 'B', 'C']:
                book = Book(title, author, level)
                self.books.append(book)
                print('# Book saved successfully')
                break
            else:
                level = input('Invalid Input ! , Please enter member level again (A/B/C): ').upper()


    def show_books(self):
        spaces = ' ' * 15 
        # max lenght of title is (15) and max length of author is (15)
        print(f'ID  | Title{" " * 10}| Author{" " * 9}| Level | Status')
        print('-' * 65)
        for book in self.books:
            s1 = 15 - len(book.title)   # spaces after title
            s2 = 15 - len(book.author)  # spaces after author
            print(f'{book.id}   | {book.title + spaces[:s1]}| {book.author + spaces[:s2]}| {book.level + " " * 4} | {"Not Available" if book.status else "Available"}')


    def borrow_book(self):
        id_member = int(input('* Enter member ID: '))
        id_book = int(input('* Enter book ID: '))
        member_level = 0
        book_level = 0
        for memb in self.members:
            if id_member == memb.id:
                member_level = memb.level
                member_name = memb.name
                index_member = self.members.index(memb)    # to return the index of the object member in the list
                break
        else:
            print('ID for member NOT Found')

        for book in self.books:
            if id_book == book.id:
                if book.status:
                    print('# The book is already borrowed')
                else:
                    book_level = book.level
                    book_title = book.title
                    index_book = self.books.index(book)
                break
        else:
            print('ID for book NOT Found')

        if member_level and book_level:
            if member_level == book_level:
                print(f'# {member_name} has borrowd the book: {book_title}')
                self.books[index_book].status = True                # access the object through the index of that object in the list
                # the list of borrowd books for every member
                # access the outter list that contains objects by the index of that required object
                # and access the inner list which is the borrowed books through the object and append the id of the book
                self.members[index_member].borrowd.append(id_book)  

            else:
                print('# This book is not appropriate for you.')                


    def return_book(self):
        id_member = int(input('* Enter member ID: '))
        id_book = int(input('* Enter book ID: '))
        flag_memb = 0
        flag_book = 0
        for memb in self.members:
            if id_member == memb.id:
                member_name = memb.name
                index_member = self.members.index(memb) 
                flag_memb = 1   
                break
        else:
            print('ID for member NOT Found')
            
        for book in self.books:
            if id_book == book.id:
                if book.status == False:
                    print('# The book is Available and not borrowed')
                else:
                    book_title = book.title
                    index_book = self.books.index(book)
                    flag_book = 1
                break
        else:
            print('ID for book NOT Found')


        '''
            1- why the (flag) >>> 
                if the user enters a value of ID that not exist then (variable index will not defined and give error) 
                so I have to be sure that ID member is existed
            
            2- why the second condition >>>   
                yahya   [book1, book2]
                ali     [book5, book6]
          
                if I have 2 members and a list of borrowed books for every member
                here is a situation >>> if the user enter a value id for (yahya) and a value id for (book5)
                then the above condition only will give >> that (yahya) return (book5) but he hasn't borrowed it, (ali) did
                so I have to be sure that the book in the borrowed list of the member
        '''
        if flag_book and flag_memb:
            if self.books[index_book].id in self.members[index_member].borrowd:
                print(f'# {member_name} has returned the book: {book_title}')
                self.books[index_book].status = False                                   # return the book to available
                self.members[index_member].borrowd.remove(self.books[index_book].id)    # remove the book id from the borrowed list
            else:
                print(f'{member_name} does not borrow this book: {book_title}')            





##################### additional method to return the list of borrowed books
    def show_borrowd(self):
        id = int(input('* Enter member ID: '))
        for memb in self.members:
            if id == memb.id:
                print(memb.borrowd)


class Member:
    id = 1
    def __init__(self, name, email, level) -> None:
        self.id = Member.id
        self.name = name
        self.email = email
        self.level = level
        Member.id += 1

        self.borrowd = []
        

class Book:
    id = 1
    def __init__(self, title, author, level) -> None:
        self.id = Book.id
        self.title = title
        self.author = author
        self.level = level
        self.status = False     # False >>> The book is available
        Book.id += 1
        


lib = Library()

menu = f'''
{'-' * 50}
1. Add Member
2. Edit Member
3. Show Members
4. Delete Member
5. Add Book
6. Show Books
7. Borrow Book
8. Return Book
9. Exit
'''

while True:
    print(menu)
    try:
        choice = int(input('Enter Your Choice: '))
    except:
        print('# Value Error, Enter a number value')

    else:        

        if choice == 1:
            lib.add_member()

        elif choice == 2:
            lib.edit_member()

        elif choice == 3:
            lib.show_members()

        elif choice == 4:
            lib.delete_member()

        elif choice == 5:
            lib.add_book()

        elif choice == 6:
            lib.show_books()

        elif choice == 7:
            lib.borrow_book()

        elif choice == 8:
            lib.return_book()

        elif choice == 9:
            break

        elif choice == 10:
            lib.show_borrowd()
        else:
            print('# Invalid Choice.')        