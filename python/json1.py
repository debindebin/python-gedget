import json
import os, sys
import redis

r = redis.Redis(host='112.126.82.150', port=6381, db=0, password='YiYidev3319')

def loadFont(filename):
	f = open(filename, encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
	setting = json.load(f)
	return setting

s = set([])
i = 0;
s2 = set([])
s3 = set([])
d = {'zdb': 95}
dir = "C:\\Users\\DCX\\Desktop\\yujia" 
for filename in os.listdir(dir):
	filepath = dir + "\\" + filename
	t = loadFont(filepath)
	for user in t:
		wxid = user["wxid"]
		if d.get(wxid) ==None:
			d[wxid] = 1;
		else:
			d[wxid] = d[wxid] +1;
for key in d:
	if d[key] ==16:
		print(key)

		# i=i+1
		# if user["wxid"] in s and user["wxid"] not in s2:
		# 	s2.add(user["wxid"])
		# elif user["wxid"] in s2:
		# 	s3.add(user["wxid"])
		# s.add(user["wxid"])
		# print(user["wxid"])
# j=0
# for wxid in s:
# 	j= j+1
# 	print(wxid)
# print(j)
# print(i)
# x=0
s4= s2-s3
for wxid in s4:
	# x= x+1
	print(wxid)
# print(x)


# i=0
# i1=0
# for user in t:
# 	i1=i1+1
# 	for u2 in t2:
# 		if(user["wxid"]==u2["wxid"]):
# 			print(user["wxid"])
# 			i=i+1
# 			continue
