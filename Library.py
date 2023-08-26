class Library:
    def __init__(self) -> None:
        self.members = []
        self.books = []

    def add_member(self):
        # self.members.append(member)
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
        spaces1 = '\t\t'
        spaces2 = '\t\t\t'
        print(f'ID  | Name{spaces1}| Email{spaces2}| Level')
        print('-' * 65)
        for memb in self.members:
            print(f'{memb.id}   | {memb.name}{spaces1}| {memb.email}{spaces2}| {memb.level}')


    def delete_member(self):
        id = int(input('* Enter member ID: '))
        for memb in self.members:
            if id == memb.id:
                self.members.remove(memb)
                print(f'# Member {memb.name} deleted successfully')
                break
        else:
            print('# Member ID NOT Found.')

class Member:
    id = 1
    def __init__(self, name, email, level) -> None:
        self.id = Member.id
        self.name = name
        self.email = email
        self.level = level
        Member.id += 1
        

class Book:
    def __init__(self, title, author, level) -> None:
        self.title = title
        self.author = author
        self.level = level
        self.id = 1
        self.borrowd = []


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
    choice = int(input('Enter Your Choice: '))

    if choice == 1:
        lib.add_member()

    elif choice == 2:
        lib.edit_member()

    elif choice == 3:
        lib.show_members()

    elif choice == 4:
        lib.delete_member()

    elif choice == 5:
        pass

    elif choice == 6:
        pass

    elif choice == 7:
        pass

    elif choice == 8:
        pass

    elif choice == 9:
        break
