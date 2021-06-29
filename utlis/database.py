book_list = []


def add_books(name,author):
    book_list.append({'name': name, 'author': author, 'read': False})


def show_books():
    return book_list


def mark_books_as_read(name):
    for book in book_list:
        if book['name'] == name:
            book['read'] = True


def delete(name):
    global book_list
    book_list = [book for book in book_list if book['name'] != name]
