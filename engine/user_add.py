import sys
import json
from functions import *

uname = sys.argv[1]
name = sys.argv[2]
lang = sys.argv[3]
genre = sys.argv[4]
read = sys.argv[5]
animals = sys.argv[6]

lang = list(lang.strip().split(','))
genre = list(genre.strip().split(','))
animals = list(animals.strip().split(','))

f = open("assets/users.json","r")
data = f.read()
data = json.loads(data)
data = dict(data)
if name in data.keys(): #checking if user name exists
	print('0')
	exit()
else: #else add it
	record = {
		name:{
			"uname" : uname,
			"lang" : lang,
			"genre" : genre,
			"read" : read,
			"animals" : animals,
		}
	}

	with open('assets/users.json') as f:
	    data = json.load(f)	    

	data.update(record)

	with open('assets/users.json', 'w') as f:
	    json.dump(data, f, indent=2)

	f.close()


#
userID = uname

#get tweets
text = getTweets(userID)
	
#setting up tone_analyzer

if text == 'error':
	print('1')
	sys.stdout.flush()
	exit()
	
if text == 'no tweet':
	tone_dict = {'Joy': 0, 'Confident': 0}
	formatted_tones = '<h5 style="color:teal;">You haven\'t posted for a while. But that does not matter. Find things below that you will like.</h5>'
else:
	tone_analysis = getTones(text)
	tone_dict = formatTones(tone_analysis)
	if not tone_dict:
		print('3')
		sys.stdout.flush()
		exit()
	formatted_tones = formatTonesHtml(tone_dict)

#recommendation
videos = getPersonalisedVideos(tone_dict, data[name])
formatted_videos = formatVideos(videos)

music = getPersonalisedMusic(tone_dict, data[name])
formatted_music = formatMusic(music)

print(str(formatted_tones)+'*/*'+str(formatted_videos)+'*/*'+str(formatted_music))

sys.stdout.flush()
