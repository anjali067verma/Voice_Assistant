import pyttsx3 # text to speech conversion
import speech_recognition as sr # speech recognition
import webbrowser # web browser
import datetime # date and time
import pyjokes # generates prgramming related jokes

def sptext():
    recognize=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        recognize.adjust_for_ambient_noise(source) # remove noise
        audio=recognize.listen(source)
        try:
            print("Recognizing...")
            data=recognize.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:    
            print("Not recognized")
sptext()            