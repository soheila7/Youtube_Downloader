# 🎬 YouTube Video Downloader using yt-dlp

Welcome to the YouTube Downloader Project! In this project, you will develop a Python application that allows users to download YouTube videos for offline viewing. Your mission is to create a Python script that takes a YouTube video URL as input and downloads the video to the user's local system. This project will provide a hands-on experience with the yt_dlp library, user input handling, and feedback mechanisms such as a download progress bar by using `tqdm`.

Users should be able to run YouTube Downloader from the command line or use it as a module in other Python scripts. Here are the basic steps to use the tool:

```
python youtube_downloader.py <youtube-url> <video-quality> <output-directory>
```

You can also use argparse to parse the command line arguments. The following is an example of how to use argparse to parse the command line arguments:

```
python youtube_downloader.py --url <youtube-url> --quality <video-quality> --output <output-directory>
```

And the video(s) will be downloaded to the specified output directory.

## ✅ Learning Objectives
By completing this project, you will:

- Learn to use the yt_dlp library to interact with YouTube content.
- Understand how to filter and select video streams based on parameters like resolution and file extension.
- Create a command-line interface (CLI) for user interaction.
- Implement a progress bar to show download progress.
- Practice exception handling for a robust application.
- Manage file input/output in Python.

## ✅ Features

- Download YouTube videos using [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Select specific **format code** (e.g., 602, 232, best, worst)
- Download only a **specific section** of the video (e.g., first 5 seconds)
- Shows real-time **progress bar**
- Set custom output file name
- All command-line arguments are **optional**

---

## How to Use the yt_dlp Library
You are encouraged to use the yt_dlp library for this project, which is a Python library for interfacing with YouTube content. It allows you to query metadata about videos, streams, and playlists; as well as download video and audio streams.

To learn more about yt_dlp, you can explore the official documentation. It will guide you through the process of using yt_dlp and help you implement the required features for the project. 

---
## 🧰 Requirements

Make sure you have the following installed:

```bash
pip install yt-dlp tqdm
```

---

## 🚀 Usage

You can run the script via terminal:

### 🔹 Basic usage (uses default values):

```bash
python downloader.py
```

### 🔹 Custom video URL and format:

```bash
python downloader.py "https://www.youtube.com/watch?v=2lAe1cqCOXo" -f 602 -s 00:00:00-00:00:05 -o myvideo.mp4
```

---

## 🧾 Command-Line Arguments

| Argument             | Description                                           | Default                        |
|----------------------|-------------------------------------------------------|--------------------------------|
| `url`                | The YouTube URL (optional)                            | `https://youtu.be/2lAe1cqCOXo` |
| `-f`, `--format_code`| Format code to download (e.g., 602, best)             | `602`                          |
| `-s`, `--section`    | Time section to download (e.g., 00:00:00-00:00:10)     | `00:00:00-00:00:05`            |
| `-o`, `--output_path`| Output file name                                      | `short_test.mp4`               |

> 💡 Use `yt-dlp -F <video_url>` to list all available formats.

---

## 📂 Example Output

```
Downloading:  100%|███████████████████| 1.23M/1.23M [00:02<00:00, 540kB/s]
✅ Download completed successfully!
Saved to: short_test.mp4
```

---

## 👨‍💻 Author

Developed by [Soheila Farahani]  
📧 Email: seihani.7@gmail.com  
📅 Last updated: May 2025

---

## 📝 License

This project is licensed under the MIT License.