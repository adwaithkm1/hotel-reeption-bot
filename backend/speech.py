import speech_recognition as sr

class SpeechRecognition:
    def recognize_speech(self, audio):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return {"transcript": text}
