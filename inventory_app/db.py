# database.py

import sqlite3

def connect():
    return sqlite3.connect("inventory.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, quantity, price)
        VALUES (?, ?, ?)
    ''', (name, quantity, price))
    conn.commit()
    conn.close()
print("db.py loaded")
print("Functions in db.py:", dir())
