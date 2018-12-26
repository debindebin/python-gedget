import urllib 
import urllib2

url = "http://182.92.114.178:8801/yuenr/skill/getSkillDetail"
parameters = {"accessToken":"id2rvbujPcZlvbFpvb8L6b6l64HN6cFr6bFf","deviceType":"1","id":"3738","versionName":"3.1.3","longitude":"0","latitude":"0"}

data = urllib.urlencode(parameters)
request=urllib2.Request(url, data)
response=urllib2.urlopen(request)
print response.read()