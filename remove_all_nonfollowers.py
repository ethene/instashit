from instagram.client import InstagramAPI
import os
import time
import random
import re

starttime=time.clock()

access_token = "331762741.e1b377f.ae281d5df63f4cb0996940d707c2df39"
api = InstagramAPI(access_token=access_token)

totalcount=api.user(331762741).counts['follows']

runtimelog="/home/was/.trace/"+"removeruntime.log"

us=0
max_tag_id=0
max_requests=155
r=0

users=set([])

while us<totalcount:
	if r>=max_requests:
		break
	if (max_tag_id == 0):
		page,next=api.user_follows( user_id = 331762741 )
	else:
		try:
			page,next=api.user_follows( user_id = 331762741, cursor=max_tag_id )

		except:
			print "cursor finished"
			break
	for user in page:
		if r>=max_requests:
			break
		if not(user.username in users):
			users.add(user.username)
			us=us+1
			print user
			print us

			try:
				rel = api.user_relationship(user_id=user.id)
				if rel.incoming_status =='none' : 
	            			api.unfollow_user(user_id=user.id)
                  			print 'removed'
					r=r+1
					time.sleep(5+random.random())
			except:
				print 'api error'
				api.unfollow_user(user_id=user.id)
				time.sleep(5+random.random())	
				r=r+1
	try:
		m_obj=re.search(r".+&cursor=(.+)", next)
		max_tag_id=m_obj.group(1)
	except:
		max_tag_id=0
		print "finish"
		
		break

runtime=time.clock()-starttime


fo = open(runtimelog, "wb")
fo.write("time\n");
fo.write(str(runtime));
fo.write("\n");
fo.write("calls\n");
fo.write(str(r));

fo.close()
