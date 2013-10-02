from instagram.client import InstagramAPI
import os
import time
import random
import re

filename="/home/bgp/DispatchDaemon/ins/"+"added.log"

access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
api = InstagramAPI(access_token=access_token)

totalcount=api.user(211585314).counts['follows']

us=0
max_tag_id=0

users=set([])

while us<totalcount:


	if (max_tag_id == 0):
		page,next=api.user_follows( user_id = 211585314 )
	else:
		try:
			page,next=api.user_follows( user_id = 211585314, cursor=max_tag_id )

		except:
			break
	for user in page:
		if not(user.username in users):
			users.add(user.username)
			us=us+1

	try:
		m_obj=re.search(r".+&cursor=(.+)", next)
		max_tag_id=m_obj.group(1)
	except:
		max_tag_id=0
		break
	

print us
print len(users)
print totalcount
