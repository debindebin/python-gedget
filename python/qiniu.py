#/usr/bin/env python
#__*__ coding: utf-8 __*__

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
#import qiniu
import datetime
import time
import os

access_key = ''
secret_key = ''

q = Auth(access_key, secret_key)

host ="pili.qiniuapi.com"

hub = "yuenr_live"
ticks = datetime.datetime.now()

url = "/v2/hubs/%s/stat/play/history/detail?time=%s" % (hub,ticks)
print(url)

# token = q.token_of_request()

# bucket_name ="yuenr-test-oss"
# ticks = datetime.datetime.now()
# key = "microSkill/" +ticks.year+"/"+ticks.month+"/" +ticks.day+"/"+int(time.time())
# print key

# token = q.upload_token(bucket_name, key, 3600)

# localfile = "E:\usr\test.png"
# key = key + os.path.splitext(localfile)[1]
# print key 

# ret, info = put_file(token, key, localfile)
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)
