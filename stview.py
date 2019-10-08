# _*_ coding: utf-8 _*_
# Author: Yufeng Lin
import urllib.request
import urllib.parse
 
def download(url, name):
    # path = "/Users/linyufeng/Desktop/EC601_5G_project"
    
    conn = urllib.request.urlopen(url)
    f = open(name,'wb')
    f.write(conn.read())
    f.close()
    print('saved')


fp = open("/Users/linyufeng/Desktop/EC601_5G_project/img/SampleCo.txt", "r")
for line in fp.readlines():
    line =  (lambda x: x[1:25])(line)
    Data = line.split('_')
    Lat = Data[0]
    Lon = Data[1]
    heading = Data[2]
    name = "/Users/linyufeng/Desktop/EC601_5G_project/img/SampleCo_" + Lat + "_" + Lon + "_" + heading + ".JPG"
    url = "https://maps.googleapis.com/maps/api/streetview?size=800x600&location=" + Lat + "," + Lon + "&heading=" +heading + "&pitch=0&key=" + ""
    
    print(name)
    #print url
    download(url, name)
 
fp.close()
