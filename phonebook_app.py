# Write a Phone Book App

phone_book = {}
close = False
while close == False:
    print()
    print('=====================')
    print('Electronic Phone Book')
    print('=====================')
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Quit')

    choice = int(input('What would you like to do? Enter 1-5: '))
    if choice == 1:
        a1 = input('Name: ')
        b1 = phone_book[a1]
        print(a1 + ': ' + b1)
    elif choice == 2:
        a2 = input('Name: ')
        b2 = input('Phone Number: ')
        phone_book[a2] = b2
        print(a2 + '\'s entry is saved.')
    elif choice == 3:
        c2 = input('Name: ')
        del phone_book[c2]
        print(c2 + '\'s entry has been deleted.')
    elif choice == 4:
        print('Here are the entries: ')
        for entry in phone_book:
            print(entry + ': ' + phone_book[entry])
    elif choice == 5:
        print('Bye')
        close = True
