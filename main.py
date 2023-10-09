import os
import shutil

# Specify the source directory containing the videos and pictures
source_directory = r''

# Create directories for videos and pictures if they don't exist
videos_directory = os.path.join(source_directory, 'videos')
pictures_directory = os.path.join(source_directory, 'pictures')

if not os.path.exists(videos_directory):
    os.mkdir(videos_directory)

if not os.path.exists(pictures_directory):
    os.mkdir(pictures_directory)

# List all files in the source directory
files = os.listdir(source_directory)

# Define a list of video file extensions (you can add more if needed)
video_extensions = ('.mp4', '.avi', '.mkv')

# Iterate through the files and move them to the appropriate directory
for file in files:
    file_path = os.path.join(source_directory, file)

    # Check if the file is a video based on its extension
    if file.lower().endswith(video_extensions):
        destination = os.path.join(videos_directory, file)
    else:
        destination = os.path.join(pictures_directory, file)

    # Move the file to the appropriate directory
    shutil.move(file_path, destination)

print('Files sorted successfully.')
