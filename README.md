# 🎬 YouTube Video Downloader using yt-dlp

This Python script allows you to download specific sections of YouTube videos with a selected format and shows a progress bar using `tqdm`.

## ✅ Features

- Download YouTube videos using [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Select specific **format code** (e.g., 602, 232, best, worst)
- Download only a **specific section** of the video (e.g., first 5 seconds)
- Shows real-time **progress bar**
- Set custom output file name
- All command-line arguments are **optional**

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