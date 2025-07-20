from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if isinstance(value ,str) and value.strip() != "":
            super().__init__(value)
        else:
            raise ValueError

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self , phone):
            phone_find = self.find_phone(phone)
            if not phone_find:
                raise ValueError
            self.phones.remove(phone_find)

    def edit_phone(self, old_phone: str, new_phone: str):
        if  not self.find_phone(old_phone):
            raise ValueError
        self.add_phone(new_phone)
        self.remove_phone(old_phone)
    def find_phone(self, phone: str) :
        for p in self.phones:
            if p.value == phone:
                  return p
        return None
             
             
             

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    def find(self , name :str):
        return self.data.get(name , None)
    def delete(self, name: str):
        if name  in self.data:
            del self.data[name]
        else:
            return None

book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


    



john = book.find("John")
john.edit_phone("1234567890", "1112223333")

  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")


# Видалення запису Jane
book.delete("Jane")