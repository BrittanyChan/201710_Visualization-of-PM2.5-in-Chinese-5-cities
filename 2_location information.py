# -*- coding:utf-8 -*-
import requests
import json

def getBaiduGeo(name):
    ak = 'P1GBDV0i0KwyWInnCxeQrDF9OFql7BOZ'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    bjsonlist = []
    address = name
    url = 'http://api.map.baidu.com/geocoder/v2/?address=' + address  + '&output=json&ak=' + ak
    json_data = requests.get(url = url, headers = head).json()
    json_geo = json_data['result']['location']
    json_geo['count'] = 0
    bjsonlist.append(json_geo)

    with open('./'+ name +'.json',"w") as f:
        f.write(str(bjsonlist))

print(getBaiduGeo(u'上海静安'))
print(getBaiduGeo(u'上海美国大使馆'))
print(getBaiduGeo(u'上海徐汇'))

print(getBaiduGeo(u'成都草堂寺'))
print(getBaiduGeo(u'成都美国大使馆'))
print(getBaiduGeo(u'成都沙河铺'))

print(getBaiduGeo(u'广州火车站'))
print(getBaiduGeo(u'广州美国大使馆'))
print(getBaiduGeo(u'广州第五中学'))

print(getBaiduGeo(u'沈阳太原街'))
print(getBaiduGeo(u'沈阳美国大使馆'))
print(getBaiduGeo(u'成都小河沿'))

print(getBaiduGeo(u'北京东四'))
print(getBaiduGeo(u'北京美国大使馆'))
print(getBaiduGeo(u'北京东四环'))
print(getBaiduGeo(u'北京农展馆'))