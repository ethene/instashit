from instagram.client import InstagramAPI
import random
import time
import sys
import re
import datetime
#import traceback

firstExc=''
lastExc=''

def err(er):
	global firstExc
	global lastExc
	if (firstExc == ''):
		firstExc=str(er)		
	lastExc=str(er)
	print er.args      # arguments stored in .args
	print er
	return 1

now = datetime.datetime.now()
hr=now.hour
if hr>12:
	hr=hr-12
delay=(hr)*10*60;
#print delay
#time.sleep(delay)

starttime = time.time()

#starttime=time.clock()

access_token = "331762741.e1b377f.ae281d5df63f4cb0996940d707c2df39"
api = InstagramAPI(access_token=access_token)

tagname=sys.argv[1]

#d - common delay
d=2 
like_probability=0.5
followstofollowedratio=0.83

media_crawl=500

max_requests=150
max_like_requests=345

maxfails=50

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
	try:
		if (max_tag_id==0):
			recent_media, next=api.tag_recent_media(tag_name=tagname, count=media_crawl)
		else:
			recent_media, next=api.tag_recent_media(tag_name=tagname, max_id=max_tag_id, count=media_crawl)
		time.sleep(d*random.random()+1)
	except Exception as er:
			err(er)
			fails=maxfails+1
			break
	calls=calls+1
	random.seed()

	m_obj=re.search(r".+max_tag_id=(.+)", next)
	if m_obj:
		max_tag_id=m_obj.group(1) 

	for media in recent_media:
		try:
	    		mediainfo=api.media(media.id)
			calls=calls+1
			time.sleep(d*random.random()+1)
		except Exception as er:
			err(er)
			continue
			print "media error"
			print media.id
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
    if (fails>maxfails):
	break

    remaining_users=remaining_users-1    
    try:
	userinfo=api.user(user.id)
	time.sleep(d*random.random()+1)
	calls=calls+1
    except Exception as er:
	err(er)
	print "user info error"
	print user.id
	fails=fails+1
    	continue

    follows=userinfo.counts['follows']*1.0
    followedby=userinfo.counts['followed_by']+1
    follow_ratio=follows/followedby

    if (follow_ratio > followstofollowedratio) :
	try:
		rel = api.user_relationship(user_id=user.id)
		calls=calls+1
		time.sleep(d*random.random()+1)
	except Exception as er:
		err(er)
		fails=fails+1
		print "getting relationships error"
		print user.id
    		continue

	if 	(rel.outgoing_status=='none') :

	        print user

		try :
			api.follow_user(user_id=user.id)
			calls=calls+1
			i=i+1
			time.sleep(d*random.random()+1)
		except Exception as er:
			err(er)
			print "following error"
			print user.id
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
			time.sleep(d*random.random()+1)
		except Exception as er:
			err(er)
			print "recent media error"
			print user.id
			fails=fails+1
			continue

		if (liked+(len(recent_media)/2)>=max_like_requests):
			break

                for media in recent_media:
        		if random.random() >like_probability : 
                		try:
					api.like_media(media.id)
					calls=calls+1
					liked=liked+1
					print "liked"	
				except Exception as er:
					err(er)
					print "liking error"
					print media.id
					fails=fails+1
					break
        	        	time.sleep(d*random.random()+1)


print "finishing"
try:
	fo = open(filename, "r+")
	line = fo.read();
	fo.close()
except Exception as er:
	err(er)
	print "file io error"
	line=0

usercount=i
i=int(line)+i

fo = open(filename, "wb")
fo.write(str(i));
fo.close()

runtime=time.time()-starttime

end = datetime.datetime.now()

fo = open(runtimelog, "wb")
fo.write("started\n");
fo.write(str(now));
fo.write("\n");
#fo.write("delay\n");
#fo.write(str(delay));
#fo.write("\n");
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
fo.write("time per user\n");
fo.write(str(runtime/(usercount+1)));
fo.write("\n");
fo.write("seconds per call\n");
fo.write(str(runtime/calls));
fo.write("\n");
fo.write("followed users\n");
fo.write(str(usercount));
fo.write("\n");
fo.write("liked:\n");
fo.write(str(liked));
fo.write("\n");
fo.write("first exception:\n");
fo.write(str(firstExc));
fo.write("\n");
fo.write("last exception:\n");
fo.write(str(lastExc));
fo.write("\n");
fo.write("finished\n");
fo.write(str(end));
fo.write("\n");
fo.close()
    

