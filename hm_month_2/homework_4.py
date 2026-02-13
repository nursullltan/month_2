class Contact:
    @classmethod
    def validate_phone_number(cls, phone_number):
        if phone_number < str(10):
            return False
        elif phone_number > str(10):
            return False
        else:
            return True

class  ContactList:
    all_contacts = []
    @classmethod
    def add_contact(cls, name, phone_number):
       if Contact.validate_phone_number(phone_number):
           Contact.validate_phone_number(phone_number)
       raise ValueError ("не верно")

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")



