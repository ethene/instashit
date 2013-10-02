from instagram.client import InstagramAPI
import random
import sys
import datetime

now = datetime.datetime.now()

access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
api = InstagramAPI(access_token=access_token)

tagname=sys.argv[1]

taginfo=api.tag(tagname) 
current_count=taginfo.media_count

lastname="/home/bgp/DispatchDaemon/ins/"+str(tagname)+"_last.log"

try:
	fo = open(lastname, "r+")
	line = fo.read();
	fo.close()
except:
	line=0

last_count=int(line)

fo = open(lastname, "wb")
fo.write(str(current_count));
fo.close()

difference = current_count-last_count


now_hour_name="/home/bgp/DispatchDaemon/ins/"+str(now.hour)+"_"+str(tagname)+"_hour.log"

fo = open(now_hour_name, "wb")
fo.write(str(difference));
fo.close()
      