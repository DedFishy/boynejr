from speech import talk
import urllib.request
import re
from pytube import YouTube
import pygame
import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("path","to","movie.mp4"))
video.audio.write_audiofile(os.path.join("path","to","movie_sound.mp3"))

pygame.mixer.init()

class Actions:
    def play(command):
        command = command.replace("play", "", 1)

        if not command.strip() == "":

            search_keyword=urllib.parse.quote(command)
            
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            playurl = "https://www.youtube.com/watch?v=" + video_ids[0]


            yt = YouTube(playurl)

            talk("Loading " + yt.title + ". This may take a while.")

            stream = yt.streams.filter(only_audio=True)[0]

            filename = "temp/yt.mp"
            
            stream.download(filename + "4")

            talk("Playing your music")
            print("Playing")
            pygame.mixer.music.load("temp/yt.mp3")
            pygame.mixer.music.play()