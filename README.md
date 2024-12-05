
# YouTube Audio Downloader

This script downloads the audio from a YouTube video and converts it to an MP3 file using the **yt-dlp** library. 

---

## Features

- Extracts the best audio format available from a YouTube video.
- Converts the audio to MP3 format (configurable to other formats such as M4A or WAV).
- Saves the downloaded audio file with the video title as the filename.
- Sets a timeout to prevent long waiting periods.

---

## Legal and Ethical Considerations

Downloading content from YouTube may violate its **Terms of Service** unless you have explicit permission from the content owner. This script is provided for educational purposes and should only be used to download content that:

1. **You own** (e.g., your own uploaded videos).
2. **Is licensed for free use** (e.g., Creative Commons or public domain content).
3. **You have explicit permission** to download from the content creator.

It is your responsibility to ensure that your use of this tool complies with all applicable laws and regulations. The creator of this script does not condone or take responsibility for any misuse.

---

## Requirements

- Python 3.6 or later
- **yt-dlp** library
- FFmpeg (installed and accessible via your system's PATH)

---

## Installation

1. Install **yt-dlp**:

   ```bash
   pip install yt-dlp
   ```

2. Install FFmpeg:

   - **Linux**: Use your package manager (e.g., `sudo apt install ffmpeg` for Ubuntu).
   - **Mac**: Use Homebrew: `brew install ffmpeg`.
   - **Windows**: Download the binaries from [FFmpeg](https://ffmpeg.org/download.html) and add them to your system PATH.

---

## Usage

1. Save the script to a file, e.g., `download_audio.py`.

2. Run the script with the YouTube URL as an argument:

   ```bash
   python download_audio.py "https://www.youtube.com/watch?v=example"
   ```

3. The audio will be downloaded and saved as an MP3 file in the `audios/` directory. The filename will match the video title.

---

## Example

```bash
python download_audio.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Output:
```
Downloaded: Veridis Quo
Finished downloading
```

---

## Notes

- Ensure your system has FFmpeg installed and properly configured.
- The script creates an `audios/` directory in the current working directory if it doesn't already exist.

---

## Troubleshooting

- **Timeout Errors**: If downloads take too long, ensure the `socket_timeout` value is appropriate or check your internet connection.
- **Missing FFmpeg**: If conversion to MP3 fails, confirm that FFmpeg is installed and in your PATH.

---

Enjoy downloading your favorite audio tracks responsibly! 🎵
