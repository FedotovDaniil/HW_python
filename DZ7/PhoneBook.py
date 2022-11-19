from PhoneBook_lib import *

phone_book = dict()

welcome()  

while True:
    menu()  
    choice = int(input("Ваш выбор: "))

    if choice == 1:  
        show(phone_book)

    elif choice == 2:  
        input_record(phone_book)

    elif choice == 3:  
        edit_record(phone_book)

    elif choice == 4:  
        delete_record(phone_book)

    elif choice == 5: 
        export_to_file(phone_book)

    elif choice == 0:
        print("Всего хорошего!")
        break

    else:
        print("Не существует")
