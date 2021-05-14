/* Tanisha Matthews
    Database Development and Use -Module 10
    */


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

DROP USER IF EXISTS 'whatabook_user'@'localhost';

------User creation
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

------Granting all  privilages to the user
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fkBook;
ALTER TABLE wishlist DROP FOREIGN KEY fkUser;

------ Drop tables if exists
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

------creating the tables 
CREATE TABLE book (
    bookID    INT             NOT NULL    AUTO_INCREMENT,
    bookName   VARCHAR(250)    NOT NULL,
    authorName      VARCHAR(250)    NOT NULL,
    descriptions     VARCHAR(700),
    PRIMARY KEY(bookID)
);

CREATE TABLE store (
    storeID  INT             NOT NULL    AUTO_INCREMENT,
    location      VARCHAR(400)    NOT NULL,
    PRIMARY KEY(storeID)
);

CREATE TABLE user (
    userID         INT         NOT NULL    AUTO_INCREMENT,
    firstName     VARCHAR(95) NOT NULL,
    lastName       VARCHAR(95) NOT NULL,
    PRIMARY KEY(userID) 
);

CREATE TABLE wishlist (
    wishlistID     INT         NOT NULL    AUTO_INCREMENT,
    userID         INT         NOT NULL,
    bookID        INT         NOT NULL,
    PRIMARY KEY (wishlistID),
    CONSTRAINT fkBook
    FOREIGN KEY (bookID)
        REFERENCES book(bookID),
    CONSTRAINT fkUser
    FOREIGN KEY (userID)
        REFERENCES user(userID)
);



/* Insert store */



INSERT INTO store(locale)
    VALUES('303 Cedar Crest Drive, Killeen,TX 76543');

/* Insert books */

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Sorcerer's Stone", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Chamber of Secrets", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Prisoner of Azkaban", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Goblet of Fire", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Order of the Phoenix", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Half Blood Prince", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Harry Potter and the Deathly Hallows", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Fantastic Beasts and Where to Find Them", "JK Rowling");

INSERT INTO book(book_name, author)
    VALUES("Quidditch Through the Ages", "JK Rowling");

/* Insert User */


INSERT INTO user(first_name, last_name)
    VALUES('Luna', 'Lovegood');

INSERT INTO user(first_name, last_name)
    VALUES('Ron', 'Weasley');

INSERT INTO user(first_name, last_name)
    VALUES('Albus', 'Dumbledore');


/* Insert Wishlist item */

INSERT INTO wishlist(bookID, userID)
    VALUES ((SELECT bookID FROM book WHERE bookName = 'Hogwarts: A History'),
	    (SELECT userID FROM user WHERE firstName = 'Albus'));

INSERT INTO wishlist(bookID, userID)
    VALUES ((SELECT bookID FROM book WHERE bookName = 'Care of Magical Creatures'),
	    (SELECT userID FROM user WHERE firstName = 'Luna'));

INSERT INTO wishlist(bookID, userID)
    VALUES ((SELECT bookID FROM book WHERE bookName = 'Transfiguration'),
	    (SELECT userID FROM user WHERE firstName = 'Ron'));   
