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
		tone_dict = {'Joy': 80, 'Confident': 20} #assigning dummy tones
		formatted_tones = '<h5 style="color:teal;">You haven\'t posted for a while. But that does not matter. Find things below that you will like.</h5>'
	else:
		tone_analysis = getTones(text)
		tone_dict = formatTones(tone_analysis)
		if not tone_dict:
			tone_dict = {'Joy': 80, 'Confident': 20} #assigning dummy tones
			formatted_tones = '<h5 style="co2or:teal;"> We could not analyze your mood. Your recent tweets are probably in some language that we do not support yet. But since you are a member of Mind Shift you can still enjoy our recommendations.</h5>'
		else:
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
