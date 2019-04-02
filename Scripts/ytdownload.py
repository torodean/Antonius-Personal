##################################################################################
## Program: ytdownload.py
## Author: Antonius Torode
## Date: 3/13/2019
## Purpose: For downloading videos from youtube then converting to mp3.
##################################################################################

from pytube import YouTube
import argparse
import moviepy.editor as mp

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--URL', help = 'Youtube URL', type = str, required = True)

args = parser.parse_args()

urlinput = args.URL

print('...Processing Youtube download for {0}'.format(urlinput))
yt = YouTube(urlinput)
title = yt.title

print('...Available streams are as follows:')
print(yt.streams.all())
stream = yt.streams.first()
print('...Downloading first stream ({0}):'.format(title))
stream.download('./ytdownloads')

print('...Finished download.')
print('...Starting converter.')

clip = mp.VideoFileClip('./ytdownloads/{0}.mp4'.format(title))
clip.audio.write_audiofile('./ytdownloads/{0}.mp3'.format(title))

print('...Finished converter.')

