import redis

r= redis.Redis(host='113.127.83.151', port=6385, db=0, password='password')
rr = redis.Redis(host='192.168.10.41', port=6379, db=0)

#ss = rr.get("HOME_PAGE_DEFINE")

#r.set("HOME_PAGE_DEFINE", ss)

print r.get("HOME_PAGE_DEFINE")
