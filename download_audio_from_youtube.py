"""
Created 10/11/2018
See README.md for details on dependencies
"""

# import packages
from __future__ import unicode_literals
import youtube_dl
import os
from dotenv import load_dotenv
import requests
import pandas as pd


def get_youtube_video_categories(api_key, region):
    """
    Get current YouTube video category IDs and descriptions

    :param api_key: YouTube Data v3 API key
    :param region: String two-character region code, e.g. "US"
    :return: Data frame of 'category_id' and 'category'
    """

    r = requests.get('https://www.googleapis.com/youtube/v3/videoCategories'
                     '?part=snippet&regionCode='+region+
                     '&key='+api_key)
    data = r.json()

    cols = ['category_id', 'category']
    lst = []
    for item in data['items']:
        category_id = item['id']
        category = item['snippet']['title']
        lst.append([category_id, category])
    df = pd.DataFrame(lst, columns=cols)

    return df


def get_popular_youtube_video_urls(api_key, category_id):
    """
    Get URLs and statistics for 50 most popular YouTube videos in a category.

    :param api_key: YouTube Data API v3 key
    :param category_id: string value for YouTube video category.
    :return: Pandas Data Frame of
            'video_id'
            'url'
            'comment_count'
            'view_count'
            'favorite_count'
            'dislike_count'
            'like_count'
    """
    r = requests.get('https://www.googleapis.com/youtube/v3/videos'
                     '?part=snippet%2Cstatistics'
                     '&chart=mostPopular'
                     '&maxResults=50'
                     '&regionCode=US'
                     '&videoCategoryId=' + category_id +
                     '&key=' + api_key)

    if r.status_code==200:
        data = r.json()

        cols = ['video_id', 'category_id', 'url', 'comment_count', 'view_count'
            , 'favorite_count', 'dislike_count', 'like_count']
        lst = []
        for item in data['items']:
            video_id = item['id']
            url = 'https://www.youtube.com/watch?v='+video_id
            view_count = item['statistics']['viewCount']
            favorite_count = item['statistics']['favoriteCount']
            try:
                comment_count = item['statistics']['commentCount']
                dislike_count = item['statistics']['dislikeCount']
                like_count = item['statistics']['likeCount']
            except KeyError:
                comment_count = None
                dislike_count = None
                like_count = None
            lst.append([video_id, category_id, url, comment_count, view_count, favorite_count, dislike_count, like_count])
        df = pd.DataFrame(lst, columns=cols)

        print('Success: Video info captures for category '+category_id)

        return df
    else:
        print('Error: API call failed for category '+category_id+', skipping')


def get_youtube_audio(url, directory):
    """
    Given a YouTube URL and a location to save to,
    retrieve the audio portion of the YouTube video.

    :param url: URL for a YouTube video
    :param directory: folder location for audio download save
    :return: file will be saved to directory
    """

    video_id = url.split("?v=", 1)[1]

    ydl_opts = {
        'format': 'bestaudio/best',
        'download_archive': 'downloaded_audio.txt',
        'outtmpl': directory+video_id+'.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# setup YouTube API call parameters
load_dotenv("C:/Users/Carolyn/.env")
YOUTUBE_API = os.getenv('YOUTUBE_API')

# get YouTube video categories for the US
categories = get_youtube_video_categories(YOUTUBE_API, 'US')

# for each category, retrieve list of URLs using YouTube API
video_info = pd.DataFrame([])
for cat in categories['category_id']:
    df = get_popular_youtube_video_urls(YOUTUBE_API, cat)
    video_info = video_info.append(df)

# write video information to file
video_info.to_csv('downloaded_video_audio.csv')

# for each URL, retrieve audio
for url in video_info['url']:
    get_youtube_audio(url, 'downloadedaudio/')