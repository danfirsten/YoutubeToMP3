import argparse
from yt_dlp import YoutubeDL

# Set up argument parser
parser = argparse.ArgumentParser(description="Download audio from a YouTube URL.")
parser.add_argument('url', type=str, help="The YouTube video URL to download audio from.")
args = parser.parse_args()

print(args)

# Options for extracting audio
options = {
    'format': 'bestaudio/best',  # Select the best available audio format
    'socket_timeout': 10,       # Set timeout to 10 seconds
    'postprocessors': [{        # Add post-processing for audio conversion
        'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
        'preferredcodec': 'mp3',      # Convert to MP3 format (change to 'm4a' or 'wav' if desired)
        'preferredquality': '192',    # Audio quality (bitrate in kbps)
    }],
    'outtmpl': 'audios/%(title)s.%(ext)s',   # Save file as "<title>.mp3"
}

# Use the URL provided as a command-line argument
url = args.url

print(url)

with YoutubeDL(options) as ydl:
    info = ydl.extract_info(url, download=True)  # Set download=True to fetch the audio file
    print(f"Downloaded: {info['title']}")
    print("Finished downloading")

