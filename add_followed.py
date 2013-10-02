from instagram.client import InstagramAPI
import random

access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
api = InstagramAPI(access_token=access_token)


for page,next in api.user_follows( user_id = 211585314, as_generator = True ):
	for follower in page:
		#print follower
		rel = api.user_relationship(user_id=follower.id)
		if rel.outgoing_status =='none' :
            		try: 
				api.follow_user(user_id=follower.id)
				
            		except:
				print 'following error'
			time.sleep(4*random.random())    
