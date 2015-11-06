from django.db import models
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.
class Tweet(models.Model):
	"""docstring for Tweet"""
	
	coordinates 	= models.CharField( max_length=255, blank = True, null = True )
	created_at 		= models.CharField( max_length=255, blank = True, null = True )
	entities 		= models.CharField( max_length=255, blank = True, null = True ) 
	geo 			= models.CharField( max_length=255, blank = True, null = True ) 
	tweet_id 		= models.CharField( max_length=255, blank = True, null = True )
	id_str 			= models.CharField( max_length=255, blank = True, null = True ) 
	lang  			= models.CharField( max_length=255, blank = True, null = True ) 
	meta			= models.CharField( max_length=255, blank = True, null = True )    
	place 			= models.CharField( max_length=255, blank = True, null = True ) 
	tweet 			= models.CharField( max_length=255, blank = True, null = True ) 
	user_created_at = models.CharField( max_length=255, blank = True, null = True ) 
	geo_enabled 	= models.CharField( max_length=255, blank = True, null = True )
	user_id 		= models.CharField( max_length=255, blank = True, null = True )
	user_id_str 	= models.CharField( max_length=255, blank = True, null = True )
	user_lang 		= models.CharField( max_length=255, blank = True, null = True )
	user_location 	= models.CharField( max_length=255, blank = True, null = True )
	user_name 		= models.CharField( max_length=255, blank = True, null = True )
	user_screen_name= models.CharField( max_length=255, blank = True, null = True ) 
	user_timezone 	= models.CharField( max_length=255, blank = True, null = True )
	processed		= models.IntegerField( default = 0 )


# class Coordinates(models.Model):
# 	type_ 			= models.CharField( max_length = 255, blank = True, null = True )

		