# Tanisha Matthews
 #   Database Development and Use -Module 10 



import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def menu():
    print("\n --Main Menu--")
    print("\n  1. Books\n  2. Store Locations\n  3. Account\n  4. Exit")

    try:
        user_selection = int(input("\nSelect from the menu: "))
        return user_selection
    except ValueError:
        print("\nInvalid input, Program Terminated ---\n")
        sys.exit(0)

def show_books(cursor_obj):
   cursor_obj.execute("SELECT bookID, bookName, authorName, descriptions FROM book")
   
   books = cursor_obj.fetchall()
   
   print("\nShowing all the Books")

   for book in books:
        print("\nBook ID: {}\nBook Name: {}\nAuthor: {}\nDescription: {}\n".format(book[0], book[1], book[2], 
        book[3])

    
def show_locations(cursor_obj):
    
    cursor_obj.execute("SELECT storeID, location FROM store")
    
    locations = cursor_obj.fetchall()

    print("\n--- STORE INFO ---: ")
    for location in locations:
        print("\nStore ID: {}\nLocation: {}\n".format(location[0], location[1]))


def validate_user():
    try:
        userID = int(input('\nPlease enter an user id: '))
        if userID < 1 or userID > 3:
            print(userID, "is not a valid user id number, please try again ---\n")
            sys.exit(0)
        return userID

    except ValueError:
        print("\nIncorrect input, please try again ---")
        sys.exit(0)

def show_account_menu():
    try:
        print("\nUSER MENU\n")
        print("1. Wishlist\n2. Add a Book\n3. Main Menu")
        selected_option = int(input('Select an option: '))
        if (selected_option < 1 or selected_option > 3):
            print("\nInvalid number.\nPlease select a valid option next time.")
            sys.exit(0)
        return selected_option

    except ValueError:
        print("\nInvalid input.\nEnd of Program.")
        sys.exit(0)
    
def display_wishlist(cursor_obj, userID):

    cursor_obj.execute("SELECT user.userID, user.firstName, user.lastName, book.bookID, book.bookName," +
                    "book.authorName " +
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.userID = user.userID " + 
                    "INNER JOIN book ON wishlist.bookID = book.bookID " + 
                    "WHERE user.userID = {}".format(userID))
    
    wishlist = cursor_obj.fetchall()

    print("\nShowing selected user's wish list.\n")
    for data in wishlist:
        print("Username: {} {}\nBook: {}\nAuthor: {}\n".format( data[1], data[2], data[4], data[5]))

def show_books_to_add(cursor_obj, userID):
    """ query the database for a list of books not in the users wishlist """
    print("Showing which books can be added in the wishlist.")
    cursor_obj.execute("SELECT bookID, bookName, authorName, descriptions FROM book WHERE bookID NOT IN (SELECT bookID FROM wishlist WHERE userID = {})".format(userID))
    available_books = cursor_obj.fetchall()

    print("\n--- DISPLAYING AVAILABLE BOOKS ---\n")
    for book in available_books:
        print("Book Id: {}\nBook Name: {}\nAuthor: {}\nDescription: {}\n".format(book[0], book[1], book[2], book[3]))

def add_book_to_wishlist(cursor_obj, bookID, userID):
    cursor_obj.execute("INSERT INTO wishlist(userID, bookID) VALUES({}, {})".format(userID, bookID))

try:
    """ try/catch block for handling potential MySQL database errors """ 
    
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()

    print("\n  Welcome to the WhatABook Application! ")
    user_selection = show_menu() 

    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)
            
        if user_selection == 3:
            userID = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    display_wishlist(cursor, userID)

                if account_option == 2:
                   
                    show_books_to_add(cursor, userID)

                    bookID = int(input("\nEnter the id of the book you want to add: "))

                    add_book_to_wishlist(cursor, userID, bookID)
                  
                    db.commit()  

                    print("\nBook id: {} was added to your wishlist!".format(bookID))

                
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please try again...")

                account_option = show_account_menu()
        
        if user_selection < 1 or user_selection > 4:
            print("\nInvalid option, please retry...")
          
        user_selection = show_menu()

    print("\n\n  Program terminated...\n\n")

 except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
    
