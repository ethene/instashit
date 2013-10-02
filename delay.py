from instagram.client import InstagramAPI
import os
import time
import random
import re
import datetime


now = datetime.datetime.now()
hr=now.hour
if hr>12:
	hr=hr-12
delay=(hr+1)*5*60;
print delay
time.sleep(delay)


access_token = "211585314.e1b377f.d45639f8eb394f2fa0ee3a8176311562"
api = InstagramAPI(access_token=access_token)


def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))


dump(api.user(211585314))