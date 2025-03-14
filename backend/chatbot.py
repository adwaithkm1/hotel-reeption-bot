import random
import google.generativeai as genai
from config import GOOGLE_API_KEY


class Chatbot:
    responses = {
        "hello": ["Hi! How can I help you?", "Hello! Need assistance?"],
        "room availability": ["We have rooms available!", "Please provide check-in and check-out dates."],
        "cancel booking": ["Sure, provide your booking ID to cancel."]
    }

    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-pro")

    def get_response(self, data):
        question = data.get('question', '').lower()

        # **Check predefined responses first**
        for key in self.responses:
            if key in question:
                return {"response": random.choice(self.responses[key])}

        # **Fallback to Gemini AI**
        response = self.model.generate_content(question)
        return {"response": response.text if response else "I don't understand."}
