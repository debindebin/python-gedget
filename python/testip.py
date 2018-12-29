#/usr/bin/env python
#__*__coding: utf-8 __*__

import hashlib
import os, sys
import redis


r = redis.Redis(host='113.127.83.151', port=6385, db=0, password='password')

list1 = r.lrange("forbidenIp",0,-1);
for ip in list1:
	# print(ip.decode('utf-8'))
	if ip.decode('utf-8') == "223.104.3.18":
		print(ip)

# agentList = r.keys("SKILL_VIEW_DAY_COUNT_7560_*")
# i = 0;
# j=0;
# for agent in agentList:
# 	j=j+1;
# 	value = agent.decode('utf-8').replace("SKILL_VIEW_DAY_COUNT_7560_","");
# 	print(value)
# 	# if int(value) >=208023:
# 	i=i+1
# print(i)
# print(j)
	# print int(value);
