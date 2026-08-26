
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

- Python 3.10 or later
- **yt-dlp** 2026.8.19 or later (see `requirements.txt`)
- FFmpeg (installed and accessible via your system's PATH)

FFmpeg is not optional. yt-dlp downloads the raw audio stream on its own, but
converting that stream to MP3 is done by FFmpeg — without it the download
succeeds and then fails at the final conversion step.

Python 3.10 is a hard floor because yt-dlp dropped 3.9 in release 2025.10.22.
On Python 3.9 `pip install yt-dlp` still succeeds, but silently installs the
last 3.9-compatible build instead of reporting an error.

---

## Installation

1. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Install FFmpeg:

   - **Linux**: Use your package manager (e.g., `sudo apt install ffmpeg` for Ubuntu).
   - **Mac**: Use Homebrew: `brew install ffmpeg`.
   - **Windows**: Download the binaries from [FFmpeg](https://ffmpeg.org/download.html) and add them to your system PATH.

---

## Usage

1. Save the script to a file, e.g., `youtubeToMP3.py`.

2. Run the script with the YouTube URL as an argument:

   ```bash
   python youtubeToMP3.py "https://www.youtube.com/watch?v=example"
   ```

3. The audio will be downloaded and saved as an MP3 file in the `audios/` directory. The filename will match the video title.

---

## Example

```bash
python youtubeToMP3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
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
- **Extraction Errors** (e.g. `The page needs to be reloaded.`, or warnings about skipped formats): almost always a stale yt-dlp. Run `pip install -U -r requirements.txt`. If the current release still fails, the nightly often carries extractor fixes ahead of it: `pip install -U --pre "yt-dlp[default]"`.
- **`No supported JavaScript runtime could be found`**: a warning, not an error, and safe to ignore while downloads succeed. If a video later fails with no formats found, installing a JS runtime (e.g. `brew install deno`) resolves it.

---

Enjoy downloading your favorite audio tracks responsibly! 🎵
