import redis

r= redis.Redis(host='182.92.114.178', port=6381, db=0)
rr = redis.Redis(host='192.168.10.41', port=6379, db=0)

#ss = rr.get("HOME_PAGE_DEFINE")

#r.set("HOME_PAGE_DEFINE", ss)

print r.get("HOME_PAGE_DEFINE")