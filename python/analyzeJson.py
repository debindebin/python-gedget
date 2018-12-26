#/usr/bin/env python
#__*__ coding: utf-8 __*__

import json

str = '{"content":"","title":"测","appointmentTime":"[1473821400,1473907800,1473994200]","income":0,"chatroomID":["1001280"],"needPlayback":"0","isNowLvbOrAptLvb":"apt","nowOnlineNum":0}'

print type(str)

strr = json.loads(str)

print type(strr)