class PhoneBook:

    def __init__(self, path: str = 'phone_db.txt'):
        self.path = path
        self.phone_book = []

    def open_phone_book(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            file = data.readlines()
            for contact in file:
                new = contact.strip().split(';')
                pb_dictionary = {}
                pb_dictionary['name'] = new[0]
                pb_dictionary['phone'] = new[1]
                pb_dictionary['comment'] = new[2]
                self.phone_book.append(pb_dictionary)


    def save_phone_book(self):
        with open(self.path, 'w', encoding='utf-8') as data:
            for item in self.phone_book:
                info = []
                for key, value in item.items():
                    info.append(value)
                data.write(';'.join(info)+'\n')



    def add_contact(self, new_contact: dict):
        self.phone_book.append(new_contact)


    def get(self):
        return self.phone_book


    def find_contact(self, contact_info: str) -> list:
        search_result = []
        for contact in self.phone_book:
            for fild in contact.values():
                if contact_info in fild:
                    search_result.append(contact)
        return search_result


    def change_contact(self, i: int, new_contact_info: dict):
        self.phone_book[i] = new_contact_info

    def delete_contact(self, i: int):
        self.phone_book.pop(i)