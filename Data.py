def run():
    menu = '''
    What action do you wish to perform? 

    1. Add user 
    2. See all
    3. Update user
    4. Remove all users
    
     Select an option: '''
    flag_Option = True

    while flag_Option:
        option = input(menu)

        if option == '1':
            print('New registration')
            file = open("Dates.txt", "a")
            ide = input('Enter id: ')
            name = input('Enter full name: ')
            number = input('Enter phone number: ')
            adress = input('Enter adress: ')

            print('User added')

            file.write(f'Id: {ide}, Name: {name}, Number: {number}, Adress: {adress} \n')
            file.close()

            flag_Option = False
            

        elif option == '2':
            print('Saved records')
            file = open("Dates.txt")

            print(file.read())

            file.close()

            flag_Option = False

        else:
            print('Enter a valid value')

        
if __name__ == '__main__':
    run()
