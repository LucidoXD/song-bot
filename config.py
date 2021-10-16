import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ''))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", "Youtube song downloader use /song {yt link} or {song name}")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/cadf0668c7823989a5168.jpg")
    OWNER = os.environ.get("OWNER", "MR_JINN_OF_TG") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
