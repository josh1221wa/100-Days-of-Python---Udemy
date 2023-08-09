import sqlite3

db = sqlite3.connect("Day 63/books-collection.db")    # This command connects to the database. If it isn't created it will create it.

cursor = db.cursor()    # Creates a cursor for the db

# cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

# These SQL statements are all very error prone so we use a library called SQLAlchemy to manage our databases.