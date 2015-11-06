import tweepy
 
#consumer key Ps23uVmAKDV411Dy2IRYy7lQg
#consumer secret d5YeK6fTsEIdO2uvqcXhcVYyfFevUhEGB4U7sGjp3E2dHOBKXE
 
#Setting up Twitter API
 
 
# Consumer keys and access tokens, used for OAuth
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
'''import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.twitter
collection=db.tweets
'''
query = 'running'
query2='swimming'
max_tweets = 5


results = tweepy.Cursor(api.search, q=query).items(max_tweets)
#results_b= tweepy.Cursor(api.search, q=query2).items(max_tweets)'''
s = 0
for r in results:
	'''import json
	with open('results.json', 'w') as fp:
		json.dump(results,fp)	
'''
	s = s + 1
	data={}
	data['coordinates']= r.coordinates
    	data['created_at']= r.created_at
	data['entities']= r.entities
	data['geo']= r.geo
	data['tweet_id']= r.id
	data['id_str']= r.id_str
	data['lang']= r.lang
	data['metadata']= r.metadata
	data['place']= r.place
	data['tweet']=r.text
	data['user_created_at']=r.user.created_at
	data['geo_enabled']= r.user.geo_enabled
	data['user_id']=r.user.id
	data['user_id_str']=r.user.id_str
	data['user_lang']=r.user.lang
	data['user_location']=r.user.location
	data['user_name']=r.user.name
	data['user_screen_name']=r.user.screen_name
	data['user_timezone']=r.user.time_zone

	pp.pprint(data)

	# print r.text
	#print r._json['text'].encode('utf-8')
	#print r._json['user']['location'].encode('utf-8')
	#if r._json['geo'] != None:
		#print r._json['geo'].encode('utf-8')
	#pp.pprint(r._json)
	'''print s
	pp.pprint(data)
	db.collection.insert(data)
	print(db.collection.find())
	'''
print s

'''
for r in results_b:
	data={}
	data['coordinates']= r.coordinates
    	data['created_at']= r.created_at
	data['entities']= r.entities
	data['geo']= r.geo
	data['tweet_id']= r.id
	data['id_str']= r.id_str
	data['lang']= r.lang
	data['metadata']= r.metadata
	data['place']= r.place
	data['tweet']=r.text
	data['user_created_at']=r.user.created_at
	data['geo_enabled']= r.user.geo_enabled
	data['user_id']=r.user.id
	data['user_id_str']=r.user.id_str
	data['user_lang']=r.user.lang
	data['user_location']=r.user.location
	data['user_name']=r.user.name
	data['user_screen_name']=r.user.screen_name
	data['user_timezone']=r.user.time_zone'''
#collection.find(
'''
		

#json_str = json.dumps(results)
#data = json.loads(json_str)
# import json
# with open('data.json', 'w') as outfile:
#     json.dump(results, outfile, sort_keys = True, indent = 4)
# data = json.load(open(results))
print("Done")
#search = api.search(term='adventure', lang='en', result_type='recent', count=100, max_id='')
'''
import pymongo
from pymongo import MongoClient
conn=pymongo.MongoClient()
print(conn)
db=conn.mydb
print(db)	
collection=db.tweets
print(collection)
collection.insert(data)
print(collection.find())
'''


#print('done')'''

