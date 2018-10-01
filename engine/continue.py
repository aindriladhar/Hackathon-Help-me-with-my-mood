import sys
import json
import random
from functions import *


name = sys.argv[1]

f = open("assets/users.json","r")
data = f.read()
data = json.loads(data)
data = dict(data)
if name in data.keys(): #checking if user name exists
	userID = data[name]['uname']

	#get tweets
	text = getTweets(userID)
	
	#setting up tone_analyzer
	
	if text == 'no tweet':
		tone_dict = {'Joy': 0, 'Confident': 0}
		formatted_tones = '<h5 style="color:teal;">You haven\'t posted for a while. But that does not matter. Find things below that you will like.</h5>'
	else:
		tone_analysis = getTones(text)
		tone_dict = formatTones(tone_analysis)
		formatted_tones = formatTonesHtml(tone_dict)

	#recommendation
	videos = getPersonalisedVideos(tone_dict, data[name])
	formatted_videos = formatVideos(videos)

	music = getPersonalisedMusic(tone_dict, data[name])
	formatted_music = formatMusic(music)

	print(str(formatted_tones)+'*/*'+str(formatted_videos)+'*/*'+str(formatted_music))

	sys.stdout.flush()

else:
	print('User not found')
