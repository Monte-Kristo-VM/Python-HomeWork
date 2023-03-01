file = []

def open_phone_book():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        print('\nФайл открыт')
        global file
        file = data.readlines()
    input('\nНажмите Enter для продолжения...\n')


def save_phone_book():
    global file
    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for line in file:
            data.write(line)
    print('\nФайл сохранен')
    input('\nНажмите Enter для продолжения...\n')

def show_phone_book():
    print('\nСписок контактов:')
    global file
    for i in file:
        print(*i.replace('\n','').split(';'))
    input('\nНажмите Enter для продолжения...\n')

def add_contact():
    print('\nДобавление контакта:\n')
    user_info = input('Введите данные нового контакта в формате:\n'
                        'Фамилия Телефон Комментарий\n')
    global file
    file.append('\n'+';'.join(user_info.split()))
    print('\nКонтакт добавлен\n')
    input('Нажмите Enter для продолжения...\n')


def change_contact():
    print('\nИзменение контакта:\n')
    contact_info = input('Введите данные которые вы хотите изменить:\n')
    global file

    count = 0
    for i in file:
        if contact_info in i:
            count += 1

    if count == 0:
        print('\nКонтакт не найден')
        input('\nНажмите Enter для продолжения...\n')

    if count == 1:
        new_contact_info = input('\nВведите новые данные:\n')
        for i in range(len(file)):
            if contact_info in file[i]:
                file[i] = file[i].replace(contact_info, new_contact_info)
                print('\nКонтакт  изменен')
                input('\nНажмите Enter для продолжения...\n')
                break

    if count > 1:
        change_contacts = []
        for i in file:
            if contact_info in i:
               change_contacts.append(i.replace('\n',''))

        print('\nКакой контакт нужно изменить?\n')
        for i in range(len(change_contacts)):
            s = ' '.join(str(change_contacts[i]).split(';'))
            print(f'{i+1}. {s}')

        change_number = input('\nВаш выбор:')
        new_contact_info = input('\nВведите новые данные:\n')
        for i in range(len(file)):
            if change_contacts[int(change_number)-1] in file[i]:
                file[i] = file[i].replace(contact_info, new_contact_info)
                print('\nКонтакт  изменен')
                input('\nНажмите Enter для продолжения...\n')
                break


def find_contact():
    print('Поиск контактов:\n')
    contact_info = input('Введите данные для поиска контакта\n')
    print('\nСписок контактов, удовлетворяющих входным данным:')
    global file
    for i in file:
        if contact_info in i:
            print(*i.replace('\n','').split(';'))
    input('\nНажмите Enter для продолжения...\n')

def delete_contact():
    print('\nУдаление контакта')
    contact_info = input('Введите данные для удаления контакта:\n')
    global file

    count = 0
    for i in file:
        if contact_info in i:
            count+=1

    if count == 0:
        print('\nКонтакт не найден')
        input('\nНажмите Enter для продолжения...\n')

    if count == 1:
        for i in range(len(file)):
            if contact_info in file[i]:
                file.pop(i)
                print('\nКонтакт удален')
                input('\nНажмите Enter для продолжения...\n')
                break

    if count > 1:
        del_contacts = []
        for i in file:
            if contact_info in i:
                del_contacts.append(i.replace('\n',''))

        print('\nКакой контакт нужно удалить?\n')
        print('0. Все')
        for i in range(len(del_contacts)):
            s = ' '.join(str(del_contacts[i]).split(';'))
            print(f'{i+1}. {s}')

        del_number = input('\nВаш выбор:')
        if del_number == '0':
            for i in del_contacts:
                for j in file:
                    if i in j:
                        file.pop(file.index(j))
            print('Контакты удалены')
        else:
            for i in file:
                if del_contacts[int(del_number)-1] in i:
                    file.pop(file.index(i))
                    break
            print('Контакт удален')

        input('\nНажмите Enter для продолжения...\n')
