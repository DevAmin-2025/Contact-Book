from src.utils import print_success, print_info, print_options


class ContactBook:
    """
    A class to manage a contact book, including creating, viewing,
    updating and deleting contacts.
    """
    def __init__(self):
        self.contacts = {}

    def create_contact(self, name: str, phone: str, email: str):
        """
        Create a contact with the provided name, phone number, and optional email.

        :param name: The name of the contact.
        :param phone: The phone number of the contact.
        :param email: The email address of the contact.
        """
        name = name.title()
        if name in self.contacts:
            print_info('\nTwo contacts can not exist with the same name.')
            return
        elif not name.split():
            print_info('\nName can not be empty.')
            return
        elif not email.split():
            email = None

        if not phone.isdigit():
            print_info('\nPhone input must be only numbers.')
            return

        self.contacts[name] = {
        'Phone': phone,
        'Email': email,
        }
        print_success('\nContact has been successfully created.')

    def view_contact(self):
        """
        Display all contacts in the contact book.
        """
        if self.contacts:
            print_info('\nList of contacts:')
            for name, info in self.contacts.items():
                print('Name:', name)
                for field, value in info.items():
                    print(f'{field}: {value}')
                print('-' * 15)
            return

        print_info('\nContact book is empty.')

    def update_contact(self, name: str, phone: str, email: str):
        """
        Update the contact with the provided name. Optionally update the phone and email.

        :param name: The name of the contact to update.
        :param phone: The new phone number for the contact.
        :param email: The new email address for the contact.
        """
        name = name.title()
        if not name in self.contacts:
            print_info('\nContact does not exist.')
            return
        if phone.isdigit():
            self.contacts[name]['Phone'] = phone
        if email.split():
            self.contacts[name]['Email'] = email

        print_success('\nContact has been successfully updated.')

    def delete_contact(self, name: str):
        """
        Delete the contact with the provided name.

        :param name: The name of the contact to be deleted.
        """
        name = name.title()
        if not name in self.contacts:
            print_info('\nContact does not exist.')
            return

        del self.contacts[name]
        print_success('\nContact has been successfully deleted.')


if __name__ == '__main__':
    book = ContactBook()
    print_info('\nWelcome to contact book application.')

    while True:
        print_options('\n1. Add Contact')
        print_options('2. View Contacts')
        print_options('3. Edit Contact')
        print_options('4. Delete Contact')
        print_options('5. Exit the application\n')

        user_choice = input('Please enter an option: ')

        if user_choice == '5':
            print_info('\nExiting the application...\n')
            break
        elif user_choice == '1':
            name = input('Please enter contact name: ')
            phone = input('Please enter contact phone: ')
            email = input('Please enter contact email. (enter blank to leave empty): ')
            book.create_contact(name, phone, email)
        elif user_choice == '2':
            book.view_contact()
        elif user_choice == '3':
            name = input('Please enter contact name: ')
            phone = input('Please enter contact phone: ')
            email = input('Please enter contact email: ')
            book.update_contact(name, phone, email)
        elif user_choice == '4':
            name = input('Please enter contact name: ')
            book.delete_contact(name)
        else:
            print_info('\nInvalid input. you must choose one of the options: [1, 2, 3, 4, 5]')
