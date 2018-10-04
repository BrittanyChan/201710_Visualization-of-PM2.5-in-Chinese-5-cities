import json
from urllib.request import urlopen, quote

#Grab the location information from Baidu API
url = 'http://api.map.baidu.com/geocoder/v2/'
output = 'json'
ak = 'P1GBDV0i0KwyWInnCxeQrDF9OFql7BOZ'
a = ['北京东四', '北京东四环', '北京农展馆', '北京美国大使馆']
b = [0, 0, 16538.19]
data = []
for i in a:
    add = quote(i)
    uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + ak  # Baidu API
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    #print(temp['result']['location']['lng'], temp['result']['location']['lat'])
    b[0] = temp['result']['location']['lng']
    b[1] = temp['result']['location']['lat']
    #print (b)
    data.append(b)
    print (data)

