
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
	max_tweets = 500
	results = tweepy.Cursor(api.search, q=keyword).items(max_tweets)
	s = 0

	l = []
	results.__dict__
	dir(results)

	results.page_iterator.__dict__
	for r in results:
		s = s + 1
		data={}
		# data['text'] = r._json['text'].encode('utf-8')
		# fix coordinate issue
		if r.coordinates != None:
			data['coordinates'] =  str(r._json['coordinates']['coordinates']) +  ' ' + str(r._json['coordinates']['coordinates'])

		else:
			data['coordinates']= r._json['coordinates']

		data['tweet']=r._json['text'].encode('utf-8')
		data['coordinates']= r._json['coordinates']
	    	data['created_at']= r._json['created_at'].encode('utf-8')

		data['geo']= r._json['geo']
		data['tweet_id']= r._json['id']
		data['id_str']= r._json['id_str'].encode('utf-8')
		data['lang']= r._json['lang'].encode('utf-8')

		data['place']= r._json['place']

		data['user_created_at']=r._json['user']['created_at'].encode('utf-8')
		data['geo_enabled']= r._json['user']['geo_enabled']
		data['user_id']=r._json['user']['id']
		data['user_id_str']=r._json['user']['id_str'].encode('utf-8')
		data['user_lang']=r._json['user']['lang'].encode('utf-8')
		data['user_location']=r._json['user']['location'].encode('utf-8')
		data['user_name']=r._json['user']['name'].encode('utf-8')
		data['user_screen_name']=r._json['user']['screen_name'].encode('utf-8')
		data['user_timezone']=r._json['user']['time_zone']
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


<<<<<<< HEAD
def index( request ):
	tweets = len(Tweet.objects.all())
	return render(request, 'index.html', locals() )

=======
>>>>>>> b3b0660220335759cbdddda53e2d33130decee9b
# def get( request ):
# 	s = Tweet.objects.all():
	
