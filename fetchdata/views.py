
# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.dispatch import receiver
from django.db import models
from django.db.models import F, Q
from django.core.files.storage import default_storage as storage

from fetchdata.models import Tweet

from fetchdata.forms import keyword

import tweepy

consumer_key='Ps23uVmAKDV411Dy2IRYy7lQg'
consumer_secret='d5YeK6fTsEIdO2uvqcXhcVYyfFevUhEGB4U7sGjp3E2dHOBKXE'
access_token='2815485672-eitb2H5XVNCA8wH8pf7lii3sk4hrWUrMLQZu2ly'
access_token_secret='lXZgILiH634fbYcED4HBF3n8IbezET9PXZB6VS0BrZKRM'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth) # use parser=tweepy.parsers.JSONParser() for fix json issue
import json
import pprint
pp=pprint.PrettyPrinter(indent=4)


def fetch_twitter_data( keyword ):
	max_tweets = 1
	results = tweepy.Cursor(api.search, q=keyword).items(max_tweets)
	s = 0

	l = []
	for r in results:
		s = s + 1
		data={}
		# data['text'] = r._json['text'].encode('utf-8')
		# fix coordinate issue
		if r.coordinates != None:
			data['coordinates'] =  r.coordinates.coordinates
		else:
			data['coordinates'] = r.coordinates

		# data['created_at']= r.created_at
		# data['entities']= r.entities
		data['geo']= r.geo
		data['tweet_id']= r.id
		data['id_str']= r.id_str
		data['lang']= r.lang
		# data['metadata']= r.metadata
		data['place']= r.place
		data['tweet']=r.text
		# data['user_created_at']=r.user.created_at
		data['geo_enabled']= r.user.geo_enabled
		data['user_id']=r.user.id
		data['user_id_str']=r.user.id_str
		data['user_lang']=r.user.lang
		data['user_location']=r.user.location
		data['user_name']=r.user.name
		data['user_screen_name']=r.user.screen_name
		data['user_timezone']=r.user.time_zone

		l.append(data)
	return l

def add(request):
	if request.method == 'POST':
		form = keyword(request.POST)
		if form.is_valid():
			print form.cleaned_data['word']
			msg = 'keyword is  : ', form.cleaned_data['word']

			l = fetch_twitter_data( form.cleaned_data['word'] )
			# Call the script function
			print l

			# Model instane

			for x in l:
				print type(x)
				t = Tweet(**x)
				t.save()

			jsondata = json.dumps(l, indent = 4)
			return HttpResponse( jsondata, content_type = 'application/json' )
	else:
		form = keyword()
	
		return render (request, 'add.html', locals() )


def index( request ):
	tweets = len(Tweet.objects.all())
	return render(request, 'index.html', locals() )

# def get( request ):
# 	s = Tweet.objects.all():
# 	return s
