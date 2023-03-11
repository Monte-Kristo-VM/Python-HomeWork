def menu() -> int:

    print('\nРабота с телефонным справочником:\n')
    print('1. Открыть файл\n'
    '2. Сохранить файл\n'
    '3. Показать контакты\n'
    '4. Добавить контакт\n'
    '5. Изменить контакт\n'
    '6. Найти контакт\n'
    '7. Удалить контакт\n'
    '8. Выход\n')

    user_selection=input('Выберите действие: ')
    if (user_selection.isdigit()):
            if (0<int(user_selection)<9):
                return int(user_selection)
            else:
                print("\nНекорректный ввод!")
    else:
        print("\nНекорректный ввод!")

def show_phone_book(phone_book: list):
    if phone_book:
        print('\nСписок контактов:\n')
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
    else:
        print('\nТелефонная книга не открыта или контакты не найдены')


def show_contact_del(phone_book: list):
    if len(phone_book)>1:
        print('\nСписок контактов:')
        print('\n0. Удалить все')
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
    else:
        print('\nСписок контактов:\n')
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')



def input_request(text: str) -> str:
    return input(f'{text}')

def new_contact() -> dict:
    name = input('\nВведите фимилию и имя контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}

def select_change_contact() -> int:
    while True:
        print('\n1. Выбрать контакт из общего списка')
        print('2. Ввести данные для поиска контакта\n')
        user_selection = input('Выберите действие: ')
        if (user_selection.isdigit()):
            if (0 < int(user_selection) < 3):
                return int(user_selection)
            else:
                print("\nНекорректный ввод!")
        else:
            print("\nНекорректный ввод!")


def change_contact(book: list) -> tuple:
    show_phone_book(book)
    choice = int(input('\nВыберите контакт, который хотите изменить: '))
    name = input('Введите новое имя (Enter - оставить без изменений): ')
    phone = input('Введите новый телефон (Enter - оставить без изменений): ')
    comment = input('Введите новый комментарий (Enter - оставить без изменений): ')
    return choice-1, {'name': name if name else book[choice-1].get('name'),
                      'phone': phone if phone else book[choice-1].get('phone'),
                      'comment': comment if comment else book[choice-1].get('comment')}

def select_to_delet():
    while True:
        choice = input('\nВыберите контакт, который хотите удалить: ')
        if choice.isdigit():
            return int(choice)-1

def press_enter():
    input('\nНажмите Enter для продолжения...\n')

def print_info(text: str):
    print(text)

def goodbye():
    print('\nДо следующей встречи!\n')


def choice_exit():
    user_selection = input('Ваш выбор: ')
    if (user_selection.isdigit()):
        if (int(user_selection) == 1):
            return int(user_selection)