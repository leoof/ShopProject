# Database - JJ, Tristan, Dominik
import sqlite3

db = sqlite3.connect('data/mydb')
cursor = db.cursor()
6	- cursor.execute('''
    CREATE TABLE items(id INTEGER PRIMARY KEY, name TEXT,
                        price TEXT, discount TEXT unique)
''')
db.commit()