import view
import phone_book

pb = phone_book.PhoneBook()

def start():
    while True:
        user_selection = view.menu()
        match user_selection:
            case 1:
                view.print_info('Открыть файл')
                pb.open_phone_book()
                view.print_info('\nТелефонная книга загружена')
                view.press_enter()
            case 2:
                view.print_info('Сохранить файл')
                # new_phone_book = pb.get()
                pb.save_phone_book()
                view.print_info('\nФайл сохранен')
                view.press_enter()
            case 3:
                view.print_info('Показать контакты')
                book = pb.get()
                view.show_phone_book(book)
                view.press_enter()
            case 4:
                view.print_info('Добавить контакт')
                new_contact = view.new_contact()
                pb.add_contact(new_contact)
                view.print_info('\nКонтакт добавлен')
                view.press_enter()
            case 5:
                view.print_info('Изменить контакт')
                new_contact_info = view.change_contact(pb.get())
                pb.change_contact(*new_contact_info)
                view.print_info('\nКонтакт изменен')
                view.press_enter()
            case 6:
                view.print_info('Найти контакт')
                contact_info = view.input_request('\nВведите данные искомого контакта: ')
                result = pb.find_contact(contact_info)
                view.show_phone_book(result)
                view.press_enter()
            case 7:
                view.print_info('Удалить контакт')
                index = view.select_to_delet(pb.get())
                pb.delete_contact(index)
                view.print_info('\nКонтакт успешно удален')
                view.press_enter()
            case 8:
                view.goodbye()
                break