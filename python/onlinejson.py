#/usr/bin/env python
#__*__ coding: utf-8 __*__

import redis
r = redis.Redis(host='182.92.114.178', port=6381, db=0)
home = r.get("HOME_PAGE_DEFINE")
print home
#home = home.replace("http://static.qiniu.yuenr.com/null", "http://static.qiniu.yuenr.com/home/1473685570349.png")


#r.set("HOME_PAGE_DEFINE", home)

#print r.get("HOME_PAGE_DEFINE")