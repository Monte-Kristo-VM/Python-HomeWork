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

    user_selection=int(input('Выберите действие: '))
    return user_selection

def show_phone_book(phone_book: list):
    if phone_book:
        print('\nСписок контактов:\n')
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
    else:
        print('\nТелефонная книга не открыта или пуста')

def input_request(text: str) -> str:
    return input(f'{text}')

def new_contact() -> dict:
    name = input('\nВведите фимилию и имя контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}

def change_contact(book: list) -> tuple:
    show_phone_book(book)
    choice = int(input('\nВыберите контакт, который хотите изменить: '))
    name = input('Введите новое имя (Enter - оставить без изменений): ')
    phone = input('Введите новый телефон (Enter - оставить без изменений): ')
    comment = input('Введите новый комментарий (Enter - оставить без изменений): ')
    return choice-1, {'name': name if name else book[choice-1].get('name'),
                      'phone': phone if phone else book[choice-1].get('phone'),
                      'comment': comment if comment else book[choice-1].get('comment')}

def select_to_delet(book: list):
    show_phone_book(book)
    return int(input('\nВыберите контакт, который хотите удалить: '))-1

def press_enter():
    input('\nНажмите Enter для продолжения...\n')

def print_info(text: str):
    print(text)

def goodbye():
    print('\nДо следующей встречи.')