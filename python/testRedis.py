#/usr/bin/env python
#__*__coding: utf-8 __*__

import redis

r = redis.Redis(host='113.127.83.151', port=6385, db=0, password='password')
#f = open("./orderNum.txt", 'r')
#lines = f.readlines()
#for line in lines:
#	userId = line.split()[0]
#	orderNum = line.split()[1]
#	r.set("USER_ORDER_NUMBER_" + userId, orderNum)
#	print r.get('USER_ORDER_NUMBER_' + userId)
	#r.delete('USER_CLICK_TIME,' + skillID)
#ff = open("./user_format.txt", 'r')
#lines = ff.readlines()
#for line in lines:
#	userId = line.split()[0]
#	clickNum = line.split()[1]
#	r.set('USER_CLICK_TIME,' + userId, clickNum)
#	print r.get('USER_CLICK_TIME,' + userId)
print r.get("HOME_PAGE_DEFINE_NEW")
