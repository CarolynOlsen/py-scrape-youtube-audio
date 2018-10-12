# YouTube Audio Analyzer README

## Purpose
This project was written to test audio analysis methods in Python. 
To create data to work with, it starts by scraping the audio from YouTube videos.
This is a CURRENTLY INCOMPLETE WORK IN PROGRESS.

## First time setup for YouTube audio scraping
The Python package used to scrape audio from YouTube videos (`youtube-dl`) has software dependencies. We used these steps to get set up:
* Download youtube-dl from:
https://yt-dl.org/
* Define youtube-dl.exe's location in system PATH environment variable.
* Download LIBAV from this link and copy the .exe and all DLL files to
the location of the youtube-dl.exe:
http://builds.libav.org/windows/release-gpl/