import os
import folium

data=[[ 39.96044083841945 , 116.47308791636841 , 23014.59 ] , [ 31.24916171001514 , 121.48789948569473 , 16538.19 ],
      [ 31.23538080348789, 121.45475555700204, 23014.59], [ 31.169152089592195, 121.44623500472937, 16538.19] ]

#Plot HeatMap
from folium.plugins import HeatMap
m = folium.Map([ 33., 113.], tiles='stamentoner', zoom_start=5)
HeatMap(data).add_to(m)
m.save(os.path.join(r'C:\Users\chenxi\Desktop', 'Heatmap.html'))


#http://m.blog.csdn.net/qq_14906811/article/details/74906275