"""
Created 10/11/2018

Use youtube-dl to extract audio from youtube video urls.

Steps for first time youtube-dl setup:
1. Downloaded youtube-dl from:
https://yt-dl.org/latest/youtube-dl.exe
2. Placed youtube-dl.exe in Program Files and added location
to system PATH environment variable.
3. Downloaded LIBAV from this link and copied .exe and all DLL files to
the location of the youtube-dl.exe:
http://builds.libav.org/windows/release-gpl/
"""

# import packages
from __future__ import unicode_literals
import youtube_dl
import os
from dotenv import load_dotenv



def get_youtube_audio(url, directory):
    """
    Given a YouTube URL and a location to save to,
    retrieve the audio portion of the YouTube video.

    :param url: URL for a YouTube video
    :param directory: folder location for audio download save
    :return: file will be saved to directory
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'download_archive': 'downloaded_audio.txt',
        'outtmpl': directory+'%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# setup YouTube API call parameters
load_dotenv(dotenv_path="C:/Users/Carolyn/.env")
YOUTUBE_API = os.getenv('YOUTUBE_API')
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# define arguments for YouTube API calls
argparser.add_argument("--q", help="Search term", default="ALS Ice Bucket Challenge")
argparser.add_argument("--max-results", help="Max results", default=25)
args = argparser.parse_args()
options = args

def playlists_list_by_channel_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlists().list(
    **kwargs
  ).execute()

  return print_response(response)

urls = playlists_list_by_channel_id(client,
        part='full sample,contentDetails',
        channelId='UCYfdidRxbB8Qhf0Nx7ioOYw',
        maxResults=25)


# get list of URLs for a channel
urls = get_video_urls_from_channel('UCYfdidRxbB8Qhf0Nx7ioOYw')

# download audio
get_youtube_audio('https://www.youtube.com/watch?v=hL2u93brqiA', 'downloadedaudio/')