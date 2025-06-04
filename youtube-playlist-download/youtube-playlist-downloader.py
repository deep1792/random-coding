import os
from yt_dlp import YoutubeDL

def download_playlist(playlist_url, download_path):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_path, '%(playlist)s', '%(playlist_index)s - %(title)s.%(ext)s'),
        'yes_playlist': True,
        'verbose': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
playlist_url = ''  # Replace with the actual playlist URL
download_path = ''  # Replace with your desired download path

print(f"Starting download of playlist: {playlist_url}")
print(f"Saving to: {download_path}")

download_playlist(playlist_url, download_path)
