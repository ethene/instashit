from instagram.client import InstagramAPI
import os
import time
import random
import re

start_time = time.time()
time.sleep(2)
access_token = "398903202.249fcce.3b3c4532d63646ed83b11046a58ea054"
api = InstagramAPI(access_token=access_token)


def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))


dump(api.user(211585314))

print time.time() - start_time, "seconds"
