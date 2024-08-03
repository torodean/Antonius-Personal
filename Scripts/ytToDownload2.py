#!/bin/python3.9
##################################################################################
## Program: ytdownload.py
## Author: Antonius Torode
## Date: 3/13/2019
## Purpose: For downloading videos from YouTube then converting to mp3.
##################################################################################

from pytubefix import Playlist
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=sy4IhE-KAEg&list=PL4871092A2348D8B3"

pl = Playlist(url)

for video in pl.videos:
    ys = video.streams.get_audio_only()
    ys.download(mp3=True) # pass the parameter mp3=True to save in .mp3