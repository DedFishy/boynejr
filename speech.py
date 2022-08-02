from multiprocessing import Process
import pyttsx3
import time
import speech_recognition as sr
import keyboard

listener = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            return command
    except sr.UnknownValueError:
        print("Timed out.")

engine = pyttsx3.init()

def talk(phrase):
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()

def set_volume(vol):
    engine.setProperty("volume", vol/100)

def get_volume():
    return engine.getProperty("volume")*100

def set_gender(gender):
    engine.setProperty("voice", engine.getProperty('voices')[gender].id)
    print(engine.getProperty('voices')[gender])

if __name__ == "__main__":

    talk("Never gonna give you up")
    talk("Never gonna let you down")