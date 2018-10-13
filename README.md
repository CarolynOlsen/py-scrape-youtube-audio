# YouTube Audio Analyzer
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/CarolynOlsen/py-youtube-audio-processing/graphs/commit-activity) [![Github all releases](https://img.shields.io/github/downloads/CarolynOlsen/py-youtube-audio-processing.js/total.svg)](https://GitHub.com/CarolynOlsen/py-youtube-audio-processing/releases/) [![GitHub stars](https://img.shields.io/github/stars/CarolynOlsen/py-youtube-audio-processing.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/CarolynOlsen/py-youtube-audio-processing/stargazers/)

## Purpose
This project was written to test audio analysis methods in Python. 
To create data to work with, it starts by scraping the audio from YouTube videos.
This is a CURRENTLY INCOMPLETE WORK IN PROGRESS.

## First time setup 
1. The Python package used to scrape audio from YouTube videos (`youtube-dl`) has software dependencies. We used these steps to get set up:
    * Download youtube-dl from: https://yt-dl.org/
    * Define youtube-dl.exe's location in system PATH environment variable.
    * Download LIBAV from this link and copy the .exe and all DLL files to the location of the youtube-dl.exe: http://builds.libav.org/windows/release-gpl/

2. Set up a YouTube API key at:
https://console.cloud.google.com/

3. After getting software dependencies and an API key taken care of, we stored our API key in a .env file. Replace the file path in the `load_dotenv()` command to your own .env location in the `download_audio_from_youtube.py` file to run it.

4. Install Python dependencies with `pip install -r requirements.txt`
