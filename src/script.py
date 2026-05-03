import sqlite3
from faker import Faker

fake = Faker()

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE
)
''')


def insert_random_users(num_users):
    for _ in range(num_users):
        email = fake.email() 
        
        cursor.execute('''
        INSERT INTO Users (email)
        VALUES (?)
        ''', (email,))
    
    conn.commit()
    print(f"{num_users} users inserted into the Users table.")

insert_random_users(5)

conn.close()
