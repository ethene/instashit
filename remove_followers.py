from instagram.client import InstagramAPI
import os
import random


access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
api = InstagramAPI(access_token=access_token)

for page,next in api.user_follows( user_id = 211585314, as_generator = True ):
	for follower in page:
		print follower
       		api.unfollow_user(user_id=follower.id)
       		print 'removed'
		time.sleep(5*random.random())