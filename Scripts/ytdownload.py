##################################################################################
## Program: ytdownload.py
## Author: Antonius Torode
## Date: 3/13/2019
## Purpose: For downloading videos from youtube then converting to mp3.
##################################################################################

from pytube import YouTube
from os import path
import argparse
import moviepy.editor as mp
import sys

# Adds arguments that can be passed with program.
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--URL', help = 'Youtube URL', type = str, required = False, default='None')
parser.add_argument('-l', '--LIST', help = 'Use list of URLs', type = str, required = False, default='None')
parser.add_argument('-v', '--verbose', help = 'Verbose Output.', required = False, action = 'store_true')

# Sets all passed arguments to program variables.
args = parser.parse_args()
urlinput = args.URL
listInput = args.LIST
verboseMode = args.verbose

downloadDirectory = 'ytdownloads'


def fileExists(fileName, subDirectory = '', fileExtension = '.txt'):
	"""
	Checks if a file exists.
	"""
	if subDirectory == '':
		file = fileName
	else:
		file = subDirectory + '/' + fileName + '.' + fileExtension
	print("...checking if {0} exists.".format(file))
	sys.stdout.flush()
	return path.exists(file)
	

def downloadUrl(url):
	"""
	Downloads a specified URL file.
	"""
	try: 
		print('...Processing Youtube download for {0}'.format(url))
		sys.stdout.flush()
		yt = YouTube(url)
		title = yt.title
		
		if fileExists(title, downloadDirectory, 'mp4'):
			print("...File already exists: {0}/{1}.mp4".format(downloadDirectory, title))
			print('...Finished download.')
		else:
			if verboseMode:
				print('...Available streams are as follows:')
				print(yt.streams.all())
				sys.stdout.flush()
			stream = yt.streams.first()
			print('...Downloading first stream ({0}):'.format(title))
			sys.stdout.flush()
			stream.download(downloadDirectory)

			print('...Finished download.')
	except Exception as ex:
		print(ex)
		print("...An error occured when downloading the specified URL.")

	convertMp4(title)

def convertMp4(title):
	"""
	Converts an mp4 file to mp3.
	"""
	try: 
		if fileExists(title, downloadDirectory, 'mp3'):
			print("...File already exists: {0}/{1}.mp3".format(downloadDirectory, title))
			print('...Finished converter.')
		else:
			print('...Starting converter for {0}.'.format(title))
			clip = mp.VideoFileClip('{0}/{1}.mp4'.format(downloadDirectory, title))
			clip.audio.write_audiofile('{0}/{1}.mp3'.format(downloadDirectory, title))
			
			print('...Finished converter.')
		
	except Exception as ex:
		print(ex)
		print("...An error occured when Converting the specified URL.")


def deleteMp4s():
	"""
	Used for deleting mp4 files after converting.
	"""
	

if urlinput != 'None' and listInput == 'None':
	downloadUrl(urlinput)
elif listInput != 'None' and urlInput == 'None':
	downloadList
else:
	print("...Nothing to convert, invalid inputs.")

print('...Finished program.')





