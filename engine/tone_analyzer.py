import sys
import json
import random
from functions import *


userID = sys.argv[1]

text = getTweets(userID)

tone_analysis = getTones(text)

tone_dict = formatTones(tone_analysis)
formatted_tones = formatTonesHtml(tone_dict)

videos = getVideos(tone_dict)
formatted_videos = formatVideos(videos)

music = getMusic(tone_dict)
formatted_music = formatMusic(music)

print(str(formatted_tones)+'*/*'+str(formatted_videos)+'*/*'+str(formatted_music))
sys.stdout.flush()
