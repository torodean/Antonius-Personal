#!/bin/python3
##################################################################################
## Program: ytdownload.py
## Author: Antonius Torode
## Date: 3/13/2019
## Purpose: For downloading videos from YouTube then converting to mp3.
##################################################################################

from pytube import YouTube
import os
import argparse
import moviepy.editor as mp
import sys

# Adds arguments that can be passed with the program.
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='YouTube URL. Enter value within quotes.', type=str)
parser.add_argument('-l', '--list', help='Use list of URLs. Input should be a text file.', type=str)
parser.add_argument('-v', '--verbose', help='Verbose Output.', action='store_true')
parser.add_argument('-k', '--keepmp4', help='Keeps the mp4 file', action='store_true')
parser.add_argument('-m', '--maxquality', help='Download highest quality video.', action='store_true')
parser.add_argument('-f', '--forcevideo', help='Force download highest quality video even without audio.', action='store_true')

# Sets all passed arguments to program variables.
args = parser.parse_args()
url_input = args.url
list_input = args.list
verbose_mode = args.verbose

download_directory = 'ytdownloads'


def file_exists(file_name, sub_directory='', file_extension='.txt'):
    """
    Checks if a file exists.
    """
    file_path = os.path.join(sub_directory, f"{file_name}.{file_extension}") if sub_directory else file_name
    print(f"...checking if {file_path} exists.")
    sys.stdout.flush()
    return os.path.exists(file_path)


def extract_highest_bitrate_itag(streams):
    """
    Extract the highest bitrate itag from the list of streams.
    """
    highest_bitrate = 0
    highest_itag = None
    for stream in streams.filter(progressive=True):
        print(stream)
        if stream.abr:
            bitrate = int(stream.abr.replace('kbps', ''))
            if bitrate > highest_bitrate:
                highest_bitrate = bitrate
                highest_itag = stream.itag
    return highest_itag


def extract_highest_quality_itag(streams):
    """
    Extract the highest quality itag from the list of streams.
    """
    highest_resolution = 0
    highest_itag = None
    for stream in streams.filter(progressive=True, file_extension='mp4'):
        print(stream)
        if stream.resolution:
            resolution = int(stream.resolution.replace('p', ''))
            if resolution > highest_resolution:
                highest_resolution = resolution
                highest_itag = stream.itag
    return highest_itag


def extract_highest_quality_itag_no_filter(streams):
    """
    Extract the highest quality itag from the list of streams without any filter.
    """
    highest_resolution = 0
    highest_itag = None
    for stream in streams.filter(file_extension='mp4'):
        print(stream)
        if stream.resolution:
            resolution = int(stream.resolution.replace('p', ''))
            if resolution > highest_resolution:
                highest_resolution = resolution
                highest_itag = stream.itag
    return highest_itag


def download_url(url):
    """
    Downloads a specified URL file.
    """
    try:
        print(f'...Processing YouTube download for {url}')
        sys.stdout.flush()
        yt = YouTube(url)
        title = yt.title
        file_name = ''.join(e for e in title if e.isalnum() or e.isspace())

        if file_exists(file_name, download_directory, 'mp4'):
            print(f"...File already exists: {download_directory}/{file_name}.mp4")
            print('...Skipping download.')
        else:
            if args.forcevideo:
                streams = yt.streams.filter(file_extension='mp4')
                itag = extract_highest_quality_itag_no_filter(streams)
            elif args.maxquality:
                streams = yt.streams.filter(progressive=True, file_extension='mp4')
                itag = extract_highest_quality_itag(streams)
            else:
                streams = yt.streams.filter(progressive=True, file_extension='mp4')
                itag = extract_highest_bitrate_itag(streams)

            stream = yt.streams.get_by_itag(itag)
            print(f'...Downloading {title} with itag {itag}')
            sys.stdout.flush()
            stream.download(download_directory, filename=f"{file_name}.mp4")
            print('...Finished download.')

        convert_mp4(file_name)
        if not args.keepmp4:
            delete_mp4s(file_name)
    except Exception as ex:
        print(ex)
        print(f"...ERROR: {ex}")


def convert_mp4(title):
    """
    Converts an mp4 file to mp3.
    """
    try:
        if file_exists(title, download_directory, 'mp3'):
            print(f"...File already exists: {download_directory}/{title}.mp3")
            print('...Skipping conversion.')
        else:
            print(f'...Starting conversion for {title}.mp4')
            mp4_path = os.path.join(download_directory, f"{title}.mp4")

            # Ensure the file is valid and not empty
            if os.path.getsize(mp4_path) == 0:
                print(f"...ERROR: {title}.mp4 is empty.")
                return

            clip = mp.AudioFileClip(mp4_path)
            clip.write_audiofile(os.path.join(download_directory, f"{title}.mp3"))
            print('...Finished conversion.')
    except Exception as ex:
        print(ex)
        print("...An error occurred when converting the specified URL.")


def delete_mp4s(title):
    """
    Used for deleting mp4 files after converting.
    """
    try:
        os.remove(os.path.join(download_directory, f"{title}.mp4"))
        print(f"...Deleted {title}.mp4")
    except Exception as ex:
        print(ex)
        print(f"...An error occurred when deleting {title}.mp4")


if not os.path.exists(download_directory):
    os.makedirs(download_directory)

if url_input and not list_input:
    download_url(url_input)
elif list_input:
    with open(list_input, "r") as file:
        for line in file:
            download_url(line.strip())
else:
    print("...Nothing to convert, invalid inputs.")

print('...Finished program.')
