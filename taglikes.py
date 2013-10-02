from instagram.client import InstagramAPI
import random
import time
import sys
import re
import datetime

now = datetime.datetime.now()
hr=now.hour
if hr>12:
	hr=hr-12
delay=(hr+1)*5*60;
print delay
time.sleep(delay)

starttime=time.clock()

access_token = "331762741.e1b377f.ae281d5df63f4cb0996940d707c2df39"
api = InstagramAPI(access_token=access_token)

tagname=sys.argv[1]

media_crawl=500

max_requests=150
max_like_requests=340

filename="/home/was/.trace/"+"added.log"
runtimelog="/home/was/.trace/"+"runtime.log"

calls=0
fails=0
crawled=0
max_tag_id=0
liked=0

users=set([])
usernames=set([])

print "looking for users"
while crawled<media_crawl:

	if (max_tag_id==0):
		recent_media, next=api.tag_recent_media(tag_name=tagname, count=media_crawl)
	else:
		recent_media, next=api.tag_recent_media(tag_name=tagname, max_id=max_tag_id, count=media_crawl)

	calls=calls+1
	random.seed()

	m_obj=re.search(r".+max_tag_id=(.+)", next)
	if m_obj:
		max_tag_id=m_obj.group(1) 

	for media in recent_media:
		try:
	    		mediainfo=api.media(media.id)
			calls=calls+1
		except:
			continue
			fails=fails+1
		if not(mediainfo.user.username in usernames):
			usernames.add(mediainfo.user.username)
		    	users.add(mediainfo.user)
			print mediainfo.user
		crawled=crawled+1

i=0
remaining_users=len(usernames)+1
  
print "checking users"
for user in users:
    if (i>=max_requests):
	break
    if (fails>50):
	break

    remaining_users=remaining_users-1    
    try:
	userinfo=api.user(user.id)
	calls=calls+1
    except:
	fails=fails+1
    	continue

    follows=userinfo.counts['follows']*1.0
    followedby=userinfo.counts['followed_by']+1
    follow_ratio=follows/followedby

    if (follow_ratio > 0.83) :
	try:
		rel = api.user_relationship(user_id=user.id)
		calls=calls+1
	except:
		fails=fails+1
    		continue

	if 	(rel.outgoing_status=='none') :

	        print user

		try :
			api.follow_user(user_id=user.id)
			calls=calls+1
			i=i+1
			time.sleep(5*random.random())
		except :
			print "following error"
			fails=fails+1
			continue
		
                usermediacount=min(7, max((max_like_requests-liked/remaining_users)*2, 3))
		print "requests left:"
		print max_like_requests-liked
		print "users left:"
		print remaining_users
		print "media count:"
		print usermediacount		
		try:
		       	recent_media, next = api.user_recent_media(user_id=user.id, count=usermediacount)
			calls=calls+1
		except :
			print "recent media error"
			fails=fails+1
			continue

		if (liked+(len(recent_media)/2)>=max_like_requests):
			break

                for media in recent_media:
        		if random.random() >0.5 : 
                		try:
					api.like_media(media.id)
					calls=calls+1
					liked=liked+1
					print "liked"	
				except:
					print "liking error"
					fails=fails+1
					break
        	        	time.sleep(5*random.random())


print "finishing"
try:
	fo = open(filename, "r+")
	line = fo.read();
	fo.close()
except:
	print "file io error"
	line=0

usercount=i
i=int(line)+i

fo = open(filename, "wb")
fo.write(str(i));
fo.close()

runtime=time.clock()-starttime

fo = open(runtimelog, "wb")
fo.write("started\n");
fo.write(str(now));
fo.write("\n");
fo.write("delay\n");
fo.write(str(delay));
fo.write("\n");
fo.write("runtime\n");
fo.write(str(runtime));
fo.write("\n");
fo.write("calls\n");
fo.write(str(calls));
fo.write("\n");
fo.write("fails\n");
fo.write(str(fails));
fo.write("\n");
fo.write("users\n");
fo.write(str(len(usernames)));
fo.write("\n");
fo.write("followed users\n");
fo.write(str(usercount));
fo.write("\n");
fo.write("liked:\n");
fo.write(str(liked));

fo.close()
    

