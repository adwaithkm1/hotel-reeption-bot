from flask import Flask, request, jsonify
from database import Database
from booking import Booking
from chatbot import Chatbot
from speech import SpeechRecognition
from auth import Auth

app = Flask(__name__)
db = Database()
booking = Booking(db)
chatbot = Chatbot()
speech = SpeechRecognition()
auth = Auth(db)

@app.route('/')
def home():
    return "Hotel Receptionist AI API is running!", 200

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return auth.register_user(data)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return auth.login_user(data)

@app.route('/book', methods=['POST'])
def book_room():
    data = request.json
    return booking.book_room(data)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    return chatbot.get_response(data)

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio = request.files['audio']
    return speech.recognize_speech(audio)

if __name__ == '__main__':
    app.run(debug=True)
