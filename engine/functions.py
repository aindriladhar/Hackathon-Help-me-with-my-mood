import tweepy
import datetime
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException
import json
import random
import sys


def getTweets(userID):
	'''
		Gets twitter username as argument and returns tweets in past 24 hours which if not found returns tweets for last 3 days. If strill not found returns error message
	'''
	ACCESS_TOKEN = "3283910042-MwMfIIkfSOMa38JnyS6MxOyoMy8gWXPnwp2WNcT"
	ACCESS_TOKEN_SECRET = "wltseduOgxkNufQl98sGSApHaQKIresdvHmbq7ChzTn4w"
	CONSUMER_KEY = "lj1kAeElOQXKoQFDAxCZsXGHt"
	CONSUMER_SECRET = "i6xLSUGmqjuMpERzk3WBru2hgVu60Hf9up6YBqjpXPnAcfkK60"

	# Authorize our Twitter credentials
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	#
	try:
		tweets = api.user_timeline(screen_name=userID, count=100, include_rts = False, tweet_mode = 'extended')
	except tweepy.TweepError as e:
		print(e.args[0][0]['message'])
		sys.stdout.flush()
		exit()
	text = [tweet.full_text for tweet in tweets if (datetime.datetime.now() - tweet.created_at).days < 1]
	if len(text) < 1:
		text = [tweet.full_text for tweet in tweets if (datetime.datetime.now() - tweet.created_at).days < 7]
	if(len(text) < 1):
		text = 'no tweet'
	return text

def getTones(text):	
	'''
		receives an array of string and uses watson to analyze the tone on each and finally return mean of the tones of each string as a dictionary
	'''

	#setting up tone_analyzer
	tone_analyzer = ToneAnalyzerV3(
	    version='2017-09-21',
	    username='5e5daadc-8086-40fa-815a-000791b673f4',
	    password='RM0UfnbeyAXT',
	    url='https://gateway.watsonplatform.net/tone-analyzer/api'
	)

	#get results from watson
	tone_analysis = []
	[tone_analysis.append(tone_analyzer.tone(
	        {'text': text[i]},
	        'application/json'
	    ).get_result()) for i in range(len(text))]

	return tone_analysis

def formatTones(tone_analysis):
	#Getting result
	tone_dict = {}
	try:
	    for i in range(len(tone_analysis)):
	        for x in tone_analysis[i]['document_tone']['tones']:
	            if x['tone_name'] not in tone_dict.keys():
	                tone_dict[x['tone_name']] = [x['score'], 1]
	            else:
	                tone_dict[x['tone_name']][0] += x['score']
	                tone_dict[x['tone_name']][1] += 1
	except WatsonApiException as ex:
	    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
	    sys.stdout.flush()

	#formatting result
	for key,val in tone_dict.items():
	    tone_dict[key] = round( ((tone_dict[key][0] / tone_dict[key][1]) * 100))
	return tone_dict

def getVideos(tone_dict):
	'''
		receives a dictionary having key val pair of tone and percentage and returns videos based on those mood
	'''

	f = open("assets/video.json","r")
	data = f.read()
	data = json.loads(data)
	data = dict(data)

	tone_list = list(tone_dict.keys())

	video_list = []
	for key in data.keys():
	    for mood in data[key]['mood']:
	        if mood in tone_list:
	            video_list.append(key)
	            break

	final = random.sample(range(1, len(video_list)), 2)
	videos = [data[video_list[final[0]]], data[video_list[final[1]]]]
	return videos

def formatTonesHtml(tone_dict):
	'''
		<div class="col s4 tones">
			<div class="percent">90%</div>
			<div class="name">Assertive</div>
		</div>
	'''
	string = ''
	for key in tone_dict.keys():
		string += '<div class="col s4 tones"><div class="percent">'+str(tone_dict[key])+'%</div><div class="name">'+key+'</div></div>'
	return string


def formatVideos(videos):	
	'''
		formats the recommended videos in html string
	'''
	vid1_link = videos[0]['link']
	vid1_name = videos[0]['name']
	vid2_link = videos[1]['link']
	vid2_name = videos[1]['name']

	string = '<div class="col s6"><iframe src="'+vid1_link+'" style="width:100%; height:200px;"></iframe><p>'+vid1_name+'</p></div><div class="col s6"><iframe src="'+vid2_link+'" style="width:100%; height:200px;"></iframe><p>'+vid2_name+'</p></div>'
	return string


def getMusic(tone_dict):
	'''
		receives a dictionary having key val pair of tone and percentage and returns music based on those mood
	'''

	f = open("assets/music.json","r")
	data = f.read()
	data = json.loads(data)
	data = dict(data)

	tone_list = list(tone_dict.keys())

	music_list = []
	for key in data.keys():
	    for mood in data[key]['mood']:
	        if mood in tone_list:
	            music_list.append(key)
	            break
	if len(music_list)<10:
		final = random.sample(range(1, len(music_list)), 5)
	else:
		final = random.sample(range(1, len(music_list)), 10)
	music = []
	for i in final:
		music.append(data[music_list[i]])
	return music

def formatMusic(music):	
	'''
		formats the recommended music in html string
	'''
	string = '<div class="carousel">'

	for i in range(len(music)):
		string += '<a class="carousel-item" href="#">'+music[i]['soundcloud']+'</a>'


	string += '</div>'
	
	return string

def getPersonalisedVideos(tone_dict, data):
	'''
		receives a dictionary having key val pair of tone and percentage and user profile and returns videos based on those mood
	'''

	f = open("assets/video.json","r")
	vids = f.read()
	vids = json.loads(vids)
	vids = dict(vids)

	tone_list = list(tone_dict.keys())

	video_list = []
	#mood filter
	for key in vids.keys():
	    for mood in vids[key]['mood']:
	        if mood in tone_list:
	            video_list.append(key)
	            break
	
	#animal filter
	final_video_list = []
	for key in video_list:
		for animal in data['animals']:
			if animal in vids[key]['things_in']:
				final_video_list.append(key)



	final = random.sample(range(1, len(final_video_list)), 2)
	videos = [vids[final_video_list[final[0]]], vids[final_video_list[final[1]]]]
	return videos

def getPersonalisedMusic(tone_dict, data):
	'''
		receives a dictionary having key val pair of tone and percentage and returns music based on those mood
	'''

	f = open("assets/music.json","r")
	music = f.read()
	music = json.loads(music)
	music = dict(music)

	tone_list = list(tone_dict.keys())

	music_list = []
	for key in music.keys():
	    for mood in music[key]['mood']:
	        if mood in tone_list:
	            music_list.append(key)
	            break

	#language filter
	music_list1 = []
	for key in music_list:
		for lang in data['lang']:
			if lang == music[key]['language']:
				music_list1.append(key)
				break

	#genre filter
	music_list = []
	for key in music_list1:
		for genre in data['genre']:
			if genre == music[key]['Genre']:
				music_list.append(key)
				break

	length = len(music_list)
	if length<10:
		final = random.sample(range(1, length), length-1)
	else:
		final = random.sample(range(1, length), 10)
	music_val = []
	for i in final:
		music_val.append(music[music_list[i]])
	return music_val