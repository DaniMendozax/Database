def run():
    menu = '''
    What action do you wish to perform? 

    1. Add user 
    2. Show all users
    3. Update an user
    4. Remove all users
    5. Exit 
    
     Select an option: '''
    while True:
        option = input(menu)
        if option == '1':
            print('New registration')
           
            file = open("dates.csv", "a")
            ide = input('Enter id: ')
            name = input('Enter full name: ')
            number = input('Enter phone number: ')
            address = input('Enter adress: ')

            print('User added')

            file.write(f'Id: {ide}, Name: {name}, Number: {number} , Adress: {address} \n')
            file.close()
            continue
             

        elif option == '2':
            print('Saved records \n')
            file = open("dates.csv")
            print(file.read())

            file.close()
            continue
 
        elif option == '3':
            numero = input("Enter the user id: ")
            if numero == numero:
                ide = input('Enter new id: ')
                name = input('Enter new full name: ')
                number = input('Enter new phone number: ')
                address = input('Enter new adress: ')
                print('Updated user')
                continue

        elif option == '4':
            delete = input("Enter the user id: ")
            if delete == delete:
                op = '''are you sure to delete this user?
                Enter 1 for deleted user or enter 2 for do not delete the user: '''
                opt = input(op)
                if opt == "1":
                    print("User deleted")
                elif opt == "2":
                    print("Goodbye")
        elif option == "5":
            break
        else:
            print("Enter a valid value")
if __name__ == '__main__':
    run()

