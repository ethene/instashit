from instagram.client import InstagramAPI
import os
import time
import random
import re

access_token = "331762741.e1b377f.ae281d5df63f4cb0996940d707c2df39"
api = InstagramAPI(access_token=access_token)


def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))


dump(api.user(211585314))