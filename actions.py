from speech import get_volume, set_gender, set_volume, talk, listen
import urllib.request
import re
import keyboard

import pyjokes

import wikipedia

from pytube import YouTube
import pygame
import os
from moviepy.editor import *

pygame.mixer.init()

class Actions:
    def play(command):
        command = command.replace("play", "", 1)

        if command.strip() != "":

            talk("Searching for your song")

            print("Making search kw")

            search_keyword=urllib.parse.quote(command)

            print("Loading site data")
            
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)

            print("Filtering videos")

            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

            print("Constructing URL")

            playurl = "https://www.youtube.com/watch?v=" + video_ids[0]


            yt = YouTube(playurl)

            talk("Loading " + yt.title + ". This may take a while.")

            stream = yt.streams.filter(only_audio=True)[0]
            
            stream.download(output_path="temp", filename="yt.mp4")

            video = AudioFileClip("temp/yt.mp4")
            video.write_audiofile("temp/yt.mp3")

            talk("Playing your music")
            print("Playing")

            pygame.mixer.music.load("temp/yt.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                if keyboard.is_pressed("space"):
                    pygame.mixer.music.pause()
                    talk("Music paused. What do you want to do?")
                    action = listen().lower().strip()
                    if action == None:
                        pygame.mixer.music.unpause()
                    else:
                        
                        if re.match("pause*", action):
                            pass
                        elif re.match("stop*", action):
                            pygame.mixer.music.stop()
                            break
                        elif re.match("set volume*", action) or re.match("volume*", action) or re.match("what volume*", action) or re.match("get volume*", action):
                            volume = [int(s) for s in action.split() if s.isdigit()]
                            if len(volume) > 0:
                                pygame.mixer.music.set_volume(volume[0]/100)
                            else:
                                talk("The current volume is " + str(pygame.mixer.music.get_volume()*100))
                            pygame.mixer.music.unpause()
                        else:
                            talk("Command not understood")
                            pygame.mixer.music.unpause()
                        
        
    def tell_joke(command):
        talk(pyjokes.get_joke())
    
    def get_wiki(command):
        command = command.replace("wikipedia", "", 1)

        if command.strip() != "":
            try:
                summary = wikipedia.page(title=wikipedia.search(command.strip())[0]).content

                summary = summary.split(".")
                talk("Article found. Hold down the listen button between sentences to stop playing the article.")
                for sentence in summary:
                    talk(sentence)
                    if keyboard.is_pressed("space"):
                        talk("Stopping article.")
                        break
            except Exception as e:
                print(e)
                talk("Couldn't find any info on that")
    
    def change_volume(command):
        volume = [int(s.replace("%", "")) for s in command.split() if s.replace("%", "").isdigit()]
        if len(volume) > 0:
            if volume[0] > 100 or volume[0] < 1:
                talk("Invalid volume")
            else:
                set_volume(volume[0])
                talk("Volume has been changed")
        else:
            talk("The current volume is " + str(int(get_volume())))
    
    def set_gender(command):
        if "female" in command or "girl" in command or "woman" in command:
            set_gender(1)
            talk("Set gender to female")
        elif "male" in command or "boy" in command or "man" in command:
            set_gender(0)
            talk("Set gender to male")
        

if __name__ == "__main__":
    Actions.play("play Never Gonna Give You Up")