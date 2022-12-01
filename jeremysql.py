import sqlite3

conn = sqlite3.connect('biblio.sqlite')
cursor = conn.cursor()

##
### Database setup
##

# drop database
dp = '''DROP TABLE IF EXISTS bookstore;'''
cursor.execute(dp)

# database creation
cq = '''CREATE TABLE bookstore 
        (id INTEGER, title TEXT, 
        price INTEGER, quantity INTEGER, 
        rating INTEGER, author TEXT);'''
cursor.execute(cq)

# database insertion
iq = '''INSERT INTO bookstore VALUES (?, 
        ?, ?, ?, 
        ?, ?);'''

data = [
    (1, "six of crows", 12.99, 7, 4, "Marilyn"),
    (2, "Zodiac Academy", 16.99, 8, 5, "Victor"),
    (3, "Scythe", 8.99, 10, 5, "Jeremy"),
    (4, "Divergent", 5.99, 5, 4, "Alex"),
    (5, "Beasts of Prey", 10.99, 20, 5, "Kimmy"),
    (6, "Roar", 5.99, 1, 4, "Christina"),
    (7, "Yolk", 4.99, 3, 3, "Alana"),
    (8, "Throne of Glass", 12.99, 20, 5, "Frances"),
    (9, "Maybe Someday", 10.99, 4, 5, "Jeff"),
    (10, "Serpent&Dove", 8.99, 2, 4, "Meiling"),
    (11, "Harry Potter", 12.99, 5, 5, "Victoria"),
    (12, "Lore", 5.99, 7, 5, "Julie"),
    (13, "The Rumor Game", 7.99, 6, 3, "Emily"),
    (14, "Ten Tiny Breaths", 8.99, 6, 5, "Telon"),
    (15, "Everless", 4.99, 6, 4, "Jessie")
    ]
cursor.executemany(iq, data)

##
### Queries
##


def menu():
    print("[1] Select all books")
    print("[2] Select all books, but order by price")
    print("[3] Select all books, but order by rating")
    print("[4] Select all books, but order by title")
    print("[5] Select all books, but order by author")

def menu_2():
    print("[1] Select all books")













    

