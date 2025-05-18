import argparse
from pathlib import Path
import yt_dlp
from tqdm import tqdm


class YouTubeDownloaderYTDLP:
    """
    A class to download YouTube videos using yt_dlp with progress tracking.

    Attributes:
        url (str): The YouTube video URL to download.
        output_path (str): The file path where the downloaded video will be saved.
        format_code (str): The yt_dlp format code (e.g., '602', 'best', 'worst').
        section (str): The video time section to download (e.g., '00:00:00-00:00:10').
    """
    def __init__(self, url, output_path="short_test.mp4", format_code="602", section="00:00:00-00:00:10"):
        """
        Initializes the YouTubeDownloaderYTDLP with video parameters.

        Args:
            url (str): YouTube video URL.
            output_path (str): Output file path or name.
            format_code (str): Format code to select video quality.
            section (str): Time segment to download from the video.
        """
        self.url = url
        self.output_path = output_path
        self.format_code = format_code  # مثل 'worst[ext=mp4]' یا '232+234'
        self.section = section  # مثل '00:00:00-00:00:10' برای دانلود فقط ۱۰ ثانیه 
        self.pbar = None
    
    def _progress_hook(self, d):
        """
        Internal progress hook function to track download progress and show a progress bar.

        Args:
            d (dict): Dictionary provided by yt_dlp with download status and metadata.
        """
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
            print("Download finished!")
    
    def download(self):
        """
        Downloads the specified YouTube video using yt_dlp with given options.
        """
        ydl_opts = {
            'format': self.format_code,
            'outtmpl': self.output_path,
            'download_sections': [f"*{self.section}"],
            'merge_output_format': 'mp4',  # فقط در صورت نیاز به ffmpeg
            'progress_hooks': [self._progress_hook],
            'quiet': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

def main():
    """
    Parses command-line arguments and triggers the video download process.
    """
    parser = argparse.ArgumentParser(
        description="Download a YouTube video at a specified quality and output path."
    )

    parser.add_argument(
        "url",
        nargs='?', # This means entering a url is optional
        default="https://youtu.be/2lAe1cqCOXo",
        help="The YouTube URL to download"
    )
    parser.add_argument(
        "-f", 
        "--format_code",
        help="The desired yt-dlp format code (e.g., 602, worst, best)",
        default="602",
        type=str
    )
    parser.add_argument(
        "-o",
        "--output_path",
        help="The output directory to save the video",
        default="short_test.mp4",
        type=str
    )
    parser.add_argument(
        "-s",
        "--section",
        help="Video time section to download (e.g., 00:00:00-00:00:05)",
        default="00:00:00-00:00:05",
        type=str
    )

    args = parser.parse_args()

    downloader = YouTubeDownloaderYTDLP(url=args.url, output_path=args.output_path, format_code=args.format_code)
    downloader.download()


if __name__ =="__main__":
    main()