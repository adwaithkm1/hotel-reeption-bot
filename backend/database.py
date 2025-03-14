import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('hotel.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS guests (
                                id INTEGER PRIMARY KEY, 
                                name TEXT, 
                                phone TEXT, 
                                email TEXT, 
                                key TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                                id INTEGER PRIMARY KEY, 
                                guest_id INTEGER, 
                                room_number INTEGER, 
                                status TEXT)''')
        self.conn.commit()
