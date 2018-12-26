#/usr/bin/env python
#__*__ coding: utf-8 __*__

from qiniu import Auth,urlsafe_base64_encode,http
import qiniu.config
#import qiniu
import datetime
import time
import os
import urllib
import urllib2




access_key = '68-wB4MzU0HYKh0LlNdhQsptearKELGLVMZ66jZO'
secret_key = 'H5vDtdpJyQYPPpHSAiouB5CceQ0_oS14caLGL8Yb'

q = Auth(access_key, secret_key)

host ="http://pili.qiniuapi.com"

hub = "yuenr_live"
ticks = datetime.datetime.now()

url = ("/v2/hubs/%s/stat/play/history/detail?time=%s" % (hub,ticks))
print(url)

token = q.token_of_request(url)
print(token)
headers = {'User-Agent': "QiniuPython/7.2.2 (Windows; AMD64; ) Python/2.7.12","Authorization":"Qiniu "+token,"Content-Type": "application/x-www-form-urlencoded"}
data = {"Authorization":token}
# result = http._get(host+url, None, q)
# print(result)
# print http.USER_AGENT