from instagram.client import InstagramAPI
import os
import time
import random

filename="/home/bgp/DispatchDaemon/ins/"+"added.log"

fo = open(filename, "r+")
line = fo.read();
#print "Read String is : ", line
fo.close()

i=int(line)

if i>100 :         
	access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
	api = InstagramAPI(access_token=access_token)

	for page,next in api.user_follows( user_id = 211585314, as_generator = True ):
		for follower in page:
			try:
				rel = api.user_relationship(user_id=follower.id)
				print follower
				if rel.incoming_status =='none' : 
	            			api.unfollow_user(user_id=follower.id)
	            			print 'removed'
		                	
			except:
				print 'api error'
				api.unfollow_user(user_id=follower.id)
			time.sleep(4*random.random())	
	os.remove(filename)
#	i=0
#	fo = open(filename, "wb")
#	fo.write(str(i));
#	fo.close()
