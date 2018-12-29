#/usr/bin/env python
#__*__ coding: utf-8 __*__

import redis
r = redis.Redis(host='113.127.83.151', port=6385, db=0, password='password')
home = r.get("HOME_PAGE_DEFINE")
print home
#home = home.replace("http://static.qiniu.yuenr.com/null", "http://static.qiniu.yuenr.com/home/1473685570349.png")


#r.set("HOME_PAGE_DEFINE", home)

#print r.get("HOME_PAGE_DEFINE")
