# Contact Book
A Python-based application to manage a contact book, including creating, viewing, updating and deleting contacts.

## Description
The contact Book is a simple yet effective way to manage personal contacts. with this application, you can add new contacts, view existing ones, update contact details and delete contacts as needed.

# ContactBook Class
The core logic of the application is implemnted in `ContactBook` class:
- The `create_contact` method allows for new contacts to be made to the `book`. Each contact must be unique by name.
- The `view_contact` method lists all contacts in the book along with their information.
- The `update_contact` method permits updates to contact information.
- The `delete_contact` method allows for existing contacts to be removed from the book.

## How to Run
1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

2. Navigate to the main project directory.
3. Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
4. Install required dependencies.
```bash
pip install -r requirements.txt
```
