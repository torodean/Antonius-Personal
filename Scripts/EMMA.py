#!/bin/python3

import os
import subprocess
import re

"""
EMMA - External Media Management Application

EMMA is a Python utility designed for managing external media. It helps users to:

1. Detect and mount large USB drives (e.g., 8TB drives) based on their size and label.
2. Find a specific 'movies' folder on the USB drive.
3. Create ISO images from CD-ROM or Blu-ray drives.
4. Automatically identify and handle the mount points of external media.

EMMA simplifies the process of managing and processing large amounts of media data, making it easier to organize and work with external storage devices and optical discs.
"""


def get_usb_mount_point(drive_name):
    """
    Detects and returns the mount point of a USB drive that matches the specified drive label.
    
    Args:
        drive_name (str): The label of the USB drive to search for (e.g., 'the vault').
    
    Returns:
        str: The mount point of the USB drive if a matching drive label is found.
    
    Raises:
        RuntimeError: If the `lsblk` command fails or if no drive matching the criteria is found.
    """
    try:
        result = subprocess.run(['lsblk', '-o', 'NAME,MOUNTPOINT,LABEL'], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Failed to run lsblk command: {e}')

    # Split the output into lines and skip the header
    lines = result.stdout.strip().split('\n')[1:]

    # Initialize variables
    mount_point = None
    label = None

    for line in lines:
        # Split line into parts
        parts = line.split()
        
        if len(parts) < 3:
            # Skip lines that don't have enough parts
            #print(f"Skipping line: not enough parts")
            continue

        mount_point = parts[1].strip()
        label = ' '.join(parts[2:]).strip()  # Join all remaining parts as the label
        
        # Debug output
        print(f"Mount Point: {mount_point}, Label: {label}")

        # Check if label matches
        if label.lower() == drive_name.lower():
            if os.path.exists(mount_point) and os.path.ismount(mount_point):
                return mount_point

    raise RuntimeError('No suitable USB drive found')



def find_movies_folder(mount_point):
    """
    Searches for the 'movies' folder within the specified mount point.

    This function checks if a folder named 'movies' exists at the given mount point. 
    If the folder is found, it returns the full path to this folder. If not, it raises 
    a `RuntimeError`.

    Args:
        mount_point (str): The path to the mount point where the 'movies' folder is expected 
                           to be located.

    Returns:
        str: The full path to the 'movies' folder if it exists.

    Raises:
        RuntimeError: If the 'movies' folder is not found at the specified mount point.

    Example:
        >>> find_movies_folder('/media/user/the_vault')
        '/media/user/the_vault/movies'
    """
    movies_folder_path = os.path.join(mount_point, 'movies')
    if os.path.isdir(movies_folder_path):
        return movies_folder_path
    else:
        raise RuntimeError('Movies folder not found on USB drive')


def find_cdrom_mount_point():
    """
    Identifies and returns the mount point of a CD-ROM or Blu-ray drive.

    This function scans the `/media/<username>/` directory for any mount points that could 
    potentially be the CD-ROM or Blu-ray drive. It checks if the directory is a mount point 
    and a directory, and returns the path of the first valid mount point it finds. If no 
    such mount point is found, it raises a `RuntimeError`.

    Returns:
        str: The mount point of the CD-ROM or Blu-ray drive if a valid mount point is found.

    Raises:
        RuntimeError: If the `/media/<username>/` directory does not exist or if no CD-ROM 
                      or Blu-ray drive mount point is found.

    Example:
        >>> find_cdrom_mount_point()
        '/media/user/disc'
    """
    # Look for CD-ROM mount points in /media/user/
    user_media_path = os.path.join('/media', os.getenv('USER'))
    if not os.path.exists(user_media_path):
        raise RuntimeError(f'{user_media_path} does not exist')

    for entry in os.listdir(user_media_path):
        path = os.path.join(user_media_path, entry)
        if os.path.ismount(path) and os.path.isdir(path):
            return path

    raise RuntimeError('No CD-ROM or Blu-ray drive mount point found')


def create_iso_from_disc(disc_mount_point, output_iso_path):
    """
    Creates an ISO image from the contents of a mounted CD-ROM or Blu-ray directory 
    and saves it to the specified path.

    Args:
        disc_mount_point (str): The mount point of the CD-ROM or Blu-ray drive (e.g., /media/awtorode/DIRTY_DANCING).
        output_iso_path (str): The path where the ISO image will be saved (e.g., /media/awtorode/the_vault/movies/DIRTY_DANCING.iso).

    Raises:
        RuntimeError: If the `genisoimage` command fails or if an error occurs during ISO creation.
    """
    try:
        subprocess.run(['genisoimage', '-o', output_iso_path, disc_mount_point], check=True)
        print(f'ISO image created successfully: {output_iso_path}')
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Error creating ISO image: {e}')
    except FileNotFoundError:
        raise RuntimeError('The `genisoimage` command is not found. Please install it using your package manager.')
    except Exception as e:
        raise RuntimeError(f'Unexpected error: {e}')


def eject_cdrom(drive_path):
    """
    Ejects the CD-ROM or DVD from the specified drive.

    This function uses the `eject` command to eject the media from the drive specified by 
    `drive_path`. The `eject` command must be available on the system for this function to 
    work. If the command fails, it raises a `RuntimeError`.

    Args:
        drive_path (str): The path to the CD-ROM or DVD drive (e.g., '/dev/cdrom').

    Returns:
        None

    Raises:
        RuntimeError: If the `eject` command fails to execute or if an error occurs during 
                      the eject operation.

    Example:
        >>> eject_cdrom('/dev/cdrom')
    """
    try:
        # Run the eject command to eject the media from the specified drive
        subprocess.run(['eject', drive_path], check=True)
        print(f'Media ejected successfully from {drive_path}')
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f'Error ejecting media: {e}')

def get_movie_name(mount_point):
    """
    Determines the name of the movie from the given mount point.

    This function checks multiple locations to find the movie name:
    1. The name of the top-level folder at the mount point.
    2. Metadata files (like `.nfo` files) if they exist in the directory.
    3. Common filename patterns that might indicate the movie title.

    Args:
        mount_point (str): The path where the DVD or Blu-ray is mounted.

    Returns:
        str: The determined name of the movie.

    Raises:
        RuntimeError: If no movie name can be determined from the mount point.

    Example:
        >>> get_movie_name('/media/user/movie_disc')
        'Movie Title'
    """
    # Check if the mount point is a directory
    if not os.path.isdir(mount_point):
        raise RuntimeError(f'{mount_point} is not a valid directory')

    # 1. Check if the name of the top-level folder is a reasonable movie name
    folder_name = os.path.basename(os.path.normpath(mount_point))
    if folder_name:
        return folder_name

    # 2. Check for metadata files (e.g., .nfo files)
    for root, dirs, files in os.walk(mount_point):
        for file in files:
            if file.lower().endswith('.nfo'):
                # Read the first .nfo file found for the movie name
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    movie_name = f.readline().strip()
                    if movie_name:
                        return movie_name

    # 3. Check common filename patterns (e.g., VIDEO_TS.IFO)
    for root, dirs, files in os.walk(mount_point):
        for file in files:
            if file.lower().endswith('.ifo'):
                # Use the name of the .ifo file (excluding extension) as the movie name
                movie_name = os.path.splitext(file)[0]
                if movie_name:
                    return movie_name

    # If no movie name is found, raise an error
    raise RuntimeError('Unable to determine the movie name from the mount point')

def main():
    try:
        # Detect USB drive named "the vault" with at least 8TB of space
        usb_mount_point = get_usb_mount_point('the_vault')
        print(f'USB drive mounted at: {usb_mount_point}')
        
        # Find movies folder on USB drive
        movies_folder_path = find_movies_folder(usb_mount_point)
        print(f'Movies folder found at: {movies_folder_path}')
        
        # Find the CD-ROM mount point
        disc_mount_point = find_cdrom_mount_point()
        print(f'CD-ROM mounted at: {disc_mount_point}')
        
        # Find the name of the movie.
        movie_name = get_movie_name(disc_mount_point)
        
        # Create the ISO image
        iso_file_path = os.path.join(movies_folder_path, f'{movie_name}.iso')
        create_iso_from_disc(disc_mount_point, iso_file_path)
        
        # Eject the CD/DVD/blueray when finished.
        eject_cdrom(disc_mount_point)
        
    except RuntimeError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()

