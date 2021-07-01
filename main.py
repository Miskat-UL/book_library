from utlis import database


def menu():
    database.create_book_table()
    user_input = input("""
        -Enter A to add books, 
        -Enter B to Retrive book information.
        -Enter D to delete books.
        -Enter R to mark book as read
        -Enter E for clear the database
        -press q to quit
        """
        )

    while user_input != 'q':
        if user_input == 'a':
            add_books()
        elif user_input == 'b':
            list_books()
        elif user_input == 'r':
            read_books()
        elif user_input == 'd':
            delete_books()
        # elif user_input == 'e':
        #     clear_data()
        else:
            print('unknown command, please try again ')

        user_input = input("""
                -Enter A to add books, 
                -Enter B to Retrive book information.
                -Enter D to delete books.
                -Enter R to mark book as read
                -Enter E for clear the database
                -press q to quit
                """
                           )


def add_books():
    name = input('Enter the book name: ')
    author = input('Enter author name: ')

    database.add_books(name, author)


def list_books():
    books = database.show_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NOO'
        print(f"{book['name']} by {book['author']}, read:{read}")


def read_books():
    name = input('Enter the book name you read: ')
    database.mark_books_as_read(name)


def delete_books():
    name = input('Enter the book name you want to remove: ')

    database.delete(name)


# def clear_data():
#     database.clear()

menu()