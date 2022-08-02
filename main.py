from processor import process
from speech import listen

def run_alexa():
    command = listen()
    print(command)
    if command != None:
        process(command.lower())

while True:
    run_alexa()