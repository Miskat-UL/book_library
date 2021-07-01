#saving data to CSV files.


book_list = 'data.txt'


def create_book_table():
    with open(book_list, 'w') as file:
        pass



create_book_table()

def add_books(name, author):
    with open(book_list, 'a') as file:
        file.write(f"{name},{author}, 0\n")


def show_books():
    with open(book_list, 'r') as file:
        list_lines = [line.strip().split(',') for line in file.readlines()]  # [[name, author, read],[name, author, read]]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in list_lines
    ]


def mark_books_as_read(name):
    books = show_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_book_again(books)


def _save_book_again(books):
    with open(book_list, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete(name):
    books = show_books()
    books = [book for book in books if book['name'] != name]
    _save_book_again(books)


# def clear():
#     with open(book_list, 'r+') as file:
#         file.truncate()