import pyttsx3 # text to speech conversion
import speech_recognition as sr # speech recognition
import webbrowser # web browser
import datetime # date and time
import pyjokes # generates prgramming related jokes

#Speech to text
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
            return data
        except sr.UnknownValueError:    
            print("Not recognized")          

#Text to speech
def texttosp(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)# voices[0] for male voice and vioces[1] for female voice
    rate=engine.getProperty('rate')
    engine.setProperty('rate',105)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':
     
     if sptext().lower()=="hey anjali":
         print("Test")