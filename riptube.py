import os
from yt_dlp import YoutubeDL

# Define the channel URL and the directory to save the Shorts
channel_url = "https://www.youtube.com/@deriv"
save_dir = r"C:\Users\iederees\Desktop\iederees tiktok\deriv"

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Configure yt-dlp options to download only Shorts (videos under 60 seconds)
ydl_opts = {
    'format': 'best',  # Download the best quality available
    'outtmpl': os.path.join(save_dir, '%(title)s.%(ext)s'),  # Save videos with their titles
    'quiet': False,  # Show progress in the console
    'no_warnings': False,  # Show warnings if any
    'match_filter': 'duration <= 60',  # Only download videos that are 60 seconds or shorter
}

# Download only Shorts from the channel
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([channel_url])

print("All Shorts downloaded successfully.")
