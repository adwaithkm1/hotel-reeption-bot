import hashlib
import random

class Auth:
    def __init__(self, db):
        self.db = db

    def register_user(self, data):
        name, phone, email = data['name'], data['phone'], data['email']
        unique_key = hashlib.sha256(f"{name}{random.randint(1000,9999)}".encode()).hexdigest()[:6]
        self.db.cursor.execute("INSERT INTO guests (name, phone, email, key) VALUES (?, ?, ?, ?)", (name, phone, email, unique_key))
        self.db.conn.commit()
        return {"message": "User registered", "key": unique_key}

    def login_user(self, data):
        email, key = data['email'], data['key']
        self.db.cursor.execute("SELECT * FROM guests WHERE email=? AND key=?", (email, key))
        user = self.db.cursor.fetchone()
        if user:
            return {"message": "Login successful", "user": user}
        return {"error": "Invalid credentials"}
