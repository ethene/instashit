from instagram.client import InstagramAPI
import random
import time
import sys
import re

starttime=time.clock()

access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
api = InstagramAPI(access_token=access_token)

tagname=sys.argv[1]
media_crawl=100

#filename="/home/bgp/DispatchDaemon/ins/"+"added.log"
#runtimelog="/home/bgp/DispatchDaemon/ins/"+"runtime.log"

calls=0
fails=0
crawled=0
max_tag_id=0

while crawled<media_crawl:

	if (max_tag_id==0):
		recent_media, next=api.tag_recent_media(tag_name=tagname, count=media_crawl)
	else:
		recent_media, next=api.tag_recent_media(tag_name=tagname, max_id=max_tag_id, count=media_crawl)

	m_obj=re.search(r".+max_tag_id=(.+)", next)
	if m_obj:
		max_tag_id=m_obj.group(1) 

	for media in recent_media:
		print media
		crawled=crawled+1

print crawled;