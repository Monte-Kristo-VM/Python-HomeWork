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
                select_change_contact = view.select_change_contact()
                if select_change_contact == 1:
                    new_contact_info = view.change_contact(pb.get())
                    pb.change_contact(*new_contact_info)
                else:
                    contact_info = view.input_request('\nВведите данные искомого контакта: ')
                    result_index = pb.find_contact_select(contact_info)
                    result = []
                    for i in range(len(result_index)):
                        result.append(result_index[i][1])
                    new_contact_info = view.change_contact(result)
                    pb.change_contact(result_index[new_contact_info[0]][0], new_contact_info[1])
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
                select_change_contact = view.select_change_contact()
                if select_change_contact == 1:
                    view.show_phone_book(pb.get())
                    index = view.select_to_delet()
                    pb.delete_contact(index)
                else:
                    contact_info = view.input_request('\nВведите данные искомого контакта: ')
                    result_index = pb.find_contact_select(contact_info)
                    result = []
                    for i in range(len(result_index)):
                        result.append(result_index[i][1])
                    if result:
                        view.show_contact_del(result)
                        choice = view.select_to_delet()
                        if choice != -1:
                            pb.delete_contact(result_index[choice][0])
                        else:
                            shift_index = 0
                            for i in range(len(result_index)):
                                pb.delete_contact(result_index[i][0]-shift_index)
                                shift_index+=1
                    else:
                        view.print_info('\nКонтакт(ы) не найден(ы)')
                view.print_info('\nКонтакт(ы) успешно удален(ы)')
                view.press_enter()
            case 8:
                pb_test = phone_book.PhoneBook()
                pb_test.open_phone_book()
                if pb_test.get() == pb.get():
                    view.goodbye()
                else:
                    view.print_info('\nТелефонная книга была изменена, хотите сохранить изменения?\n'
                                    '\n1. Да\n'
                                    '2. Нет\n')
                    choice = view.choice_exit()
                    if (choice == 1):
                        pb.save_phone_book()
                        view.print_info('\nФайл сохранен')
                        view.goodbye()
                    else:
                        view.goodbye()
                break