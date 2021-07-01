# #saving data to CSV files.
#
import sqlite3
#
#
#
# book_list = 'data.txt'
#
#
# def create_book_table():
#     with open(book_list, 'w') as file:
#         pass
#
#
#
# create_book_table()
#
# def add_books(name, author):
#     with open(book_list, 'a') as file:
#         file.write(f"{name},{author}, 0\n")
#
#
# def show_books():
#     with open(book_list, 'r') as file:
#         list_lines = [line.strip().split(',') for line in file.readlines()]  # [[name, author, read],[name, author, read]]
#
#     return [
#         {'name': line[0], 'author': line[1], 'read': line[2]}
#         for line in list_lines
#     ]
#
#
# def mark_books_as_read(name):
#     books = show_books()
#     for book in books:
#         if book['name'] == name:
#             book['read'] = '1'
#     _save_book_again(books)
#
#
# def _save_book_again(books):
#     with open(book_list, 'w') as file:
#         for book in books:
#             file.write(f"{book['name']},{book['author']},{book['read']}\n")
#
#
# def delete(name):
#     books = show_books()
#     books = [book for book in books if book['name'] != name]
#     _save_book_again(books)


# def clear():
#     with open(book_list, 'r+') as file:
#         file.truncate()


#saving data to SqLite database



def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key , author text, read integer )')

    connection.commit()
    connection.close()



def add_books(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO books VALUES(?,?, 0)", (name, author)) # do not use F string in database insertion it is not safe
    connection.commit()
    connection.close()



def show_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author':row[1], 'read': [2]} for row in cursor.fetchall()]
    connection.close()
    return books


def mark_books_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE books set read=1 WHERE name=?", (name, ))
    connection.commit()
    connection.close()


# def _save_book_again(books):
#     with open(book_list, 'w') as file:
#         for book in books:
#             file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name, ))
    connection.commit()
    connection.close()