from instagram.client import InstagramAPI
import os
import time
import random
import re

access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
api = InstagramAPI(access_token=access_token)

totalcount=api.user(211585314).counts['follows']

us=0
max_tag_id=0
max_requests=160
r=0

users=set([])

while us<totalcount:
	if r>=max_requests:
		break
	if (max_tag_id == 0):
		page,next=api.user_follows( user_id = 211585314 )
	else:
		try:
			page,next=api.user_follows( user_id = 211585314, cursor=max_tag_id )

		except:
			print "cursor finished"
			break
	for user in page:
		if not(user.username in users):
			users.add(user.username)
			us=us+1
			print user

			try:
				rel = api.user_relationship(user_id=user.id)
				if rel.incoming_status =='none' : 
	            			api.unfollow_user(user_id=user.id)
                    			print 'removed'
					r=r+1
					time.sleep(1+random.random())	
		                	
			except:
				print 'api error'
				api.unfollow_user(user_id=user.id)
				time.sleep(1+random.random())	


	try:
		m_obj=re.search(r".+&cursor=(.+)", next)
		max_tag_id=m_obj.group(1)
	except:
		max_tag_id=0
		print "finish"
		
		break
print us
