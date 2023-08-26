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
        pass
    
    def show_members(self):
        spaces = '\t\t\t'
        print(f'ID  | Name{spaces}| Email{spaces}| Level')
        for memb in self.members:
            print(f'{self.members.index(memb) + 1}   | {memb.name}{spaces}| {memb.email}{spaces}| {memb.level}')

    def delete_member(self):
        pass

class Member:
    def __init__(self, name, email, level) -> None:
        self.name = name
        self.email = email
        self.level = level
        self.id = 1

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
        pass

    elif choice == 3:
        lib.show_members()

    elif choice == 4:
        pass

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
