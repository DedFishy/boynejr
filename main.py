from processor import process
from speech import listen
import keyboard

def run_boynejr():
    if keyboard.is_pressed("space"):
        command = listen()
        print(command)
        if command != None:
            process(command.lower())

while True:
    run_boynejr()