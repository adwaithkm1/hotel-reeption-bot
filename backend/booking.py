class Booking:
    def __init__(self, db):
        self.db = db

    def book_room(self, data):
        guest_id, room_number = data['guest_id'], data['room_number']
        self.db.cursor.execute("SELECT * FROM bookings WHERE room_number=? AND status='booked'", (room_number,))
        if self.db.cursor.fetchone():
            return {"error": "Room already booked"}
        self.db.cursor.execute("INSERT INTO bookings (guest_id, room_number, status) VALUES (?, ?, 'booked')", (guest_id, room_number))
        self.db.conn.commit()
        return {"message": f"Room {room_number} booked successfully"}
