def ask_line_number():
    line_number = int(input('Введите индекс контакта для копирования: '))
    return line_number

def ask_data():
    contact_data = {
        'name': input('Введите имя: '),
        'surename' : input('Введите фамилию: '),
        'phone_number': input('Введите номер телефона: ')
}
    return contact_data

def ask_search_query():
    search_str = input('Поиск: ')
    return search_str

def show_phone_book():      # command == 1
    phone_book = open('phone_book.txt', 'r', encoding = 'utf-8')
    result = phone_book.read()
    phone_book.close()
    result = result.split('\n')
    result = list(enumerate(result))
    result.pop()
    for i in range(len(result)):
        print(*result[i]) 
    

def add_new_contact():      # command == 2
    contact = ask_data()
    with open('phone_book.txt', 'a', encoding = 'utf-8') as phone_book:
        for value in contact.values():
            phone_book.write(value)
            phone_book.write(' ')
        phone_book.write('\n')
        print('Контакт успешно записан')
    return True

def search():    #command == 3
    search_string = ask_search_query()
    phone_book = open('phone_book.txt', 'r', encoding = 'utf-8')
    for line in phone_book:
        if search_string in line:
            print(line)
    if search_string not in phone_book.read():
        print('404')
    phone_book.close()

def copy():     #command == 4
    with open('phone_book.txt', 'r', encoding = 'utf-8') as phone_book:
        phone_book_list = phone_book.readlines()
        show_phone_book()
        line_number = ask_line_number()
        copy_str = phone_book_list[line_number]
    with open('copy_phone_book.txt', 'w', encoding = 'utf-8') as phone_book_2:  
        phone_book_2.write(copy_str)
    return True

def main():
    command = 1
    print('Введите 1 чтобы показать все контакты')
    print('Введите 2 чтобы добавить новый контакт')
    print('Введите 3 чтобы найти контакт')
    print('Введите 4 для копирования контакта')
    print('Введите 0 чтобы выйти из меню')
    while command != 0:
        command = int(input('Введите число от 0 до 4: '))
        if command == 1:
            show_phone_book()
        elif command == 2:
            add_new_contact()
        elif command == 3:
            search()
        elif command == 4:
            copy()
        elif command == 0:
            print('Вы вышли из меню')
        else:
            print('Неверная команда')
main()

