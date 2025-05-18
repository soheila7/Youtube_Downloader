import streamlit as st
import yt_dlp
from tqdm import tqdm
from pathlib import Path
import tempfile
import os


class YouTubeDownloaderYTDLP:
    def __init__(self, url, output_path="short_test.mp4", format_code="602", section="00:00:00-00:00:05"):
        self.url = url
        self.output_path = output_path
        self.format_code = format_code
        self.section = section
        self.pbar = None

    def _progress_hook(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)

            if total_bytes is not None:
                if self.pbar is None:
                    self.pbar = tqdm(total=total_bytes, unit='B', unit_scale=True, desc='Downloading')
                self.pbar.update(downloaded - self.pbar.n)

        elif d['status'] == 'finished':
            if self.pbar:
                self.pbar.close()
                self.pbar = None
            filename = d.get('filename', self.output_path)
            st.success(f"✅ Download completed successfully!\nSaved to: {filename}")

    def download(self):
        ydl_opts = {
            'format': self.format_code,
            'outtmpl': self.output_path,
            'download_sections': [f"*{self.section}"],
            'merge_output_format': 'mp4',
            'progress_hooks': [self._progress_hook],
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
        return self.output_path


# Streamlit UI
st.set_page_config(page_title="🎬 YouTube Downloader", layout="centered")

st.title("🎬 YouTube Downloader with yt-dlp")
st.markdown("Download a specific section of a YouTube video in a selected format.")

url = st.text_input("📺 YouTube URL", value="https://youtu.be/2lAe1cqCOXo")
format_code = st.text_input("🎞️ Format Code (e.g. 602)", value="602")
section = st.text_input("⏱️ Section (start-end, e.g. 00:00:00-00:00:05)", value="00:00:00-00:00:05")
output_name = st.text_input("💾 Output file name (e.g. output.mp4)", value="short_test.mp4")

if st.button("⬇️ Start Download"):
    with st.spinner("Downloading..."):
        downloader = YouTubeDownloaderYTDLP(
            url=url,
            format_code=format_code,
            section=section,
            output_path=output_name
        )
        filepath = downloader.download()

        if Path(filepath).exists():
            with open(filepath, 'rb') as f:
                st.download_button(label="📥 Download video", data=f, file_name=output_name, mime="video/mp4")