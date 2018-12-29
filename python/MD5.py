#/usr/bin/env python
#__*__coding: utf-8 __*__

import hashlib
import os, sys
import redis

#r = redis.Redis(host='113.127.83.151', port=6385, db=0, password='password')
r = redis.Redis(host='113.127.83.151', port=6385, db=0, password='password')

def getBigFileMD5(filepath):
	if os.path.isfile(filepath):
		md5obj = hashlib.md5()
		maxbuf = 8192
		f = open(filepath, 'rb')
		while  True:
			buf = f.read(maxbuf)
			if not buf:
				break;
			md5obj.update(buf)
		f.close()
		hash = md5obj.hexdigest()
		return str(hash).lower()
	return None

# dir = "C:\\Users\\DCX\\Desktop\\output\\output" 
# for filename in os.listdir(dir):
# 	filepath = dir + "\\" + filename
# 	keyname = filepath.split("\\")[-1]
# 	keyname = keyname.replace(".apk", "")
# 	md5 = getBigFileMD5(filepath)
# 	print (keyname + ">>>md5>>>" + md5)
# 	r.set(keyname, md5)
# 	print (r.get(keyname))

filepath = "C:\\Users\\DCX\\Desktop\\\Yuenr-3.4.1-OPPO.apk"
filename =  filepath.split("\\")[-1]
filename = filename.replace(".apk", "")
md5 = getBigFileMD5(filepath)
print (filename)
print(md5)
r.set(filename, md5)
print(r.get(filename))
