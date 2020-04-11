import requests
import urllib.request
from bs4 import BeautifulSoup
from time import sleep
for c in range(1041031,1168159):
    d = str(c+1000)
    for i in range(15637428551,156374285817):
        b=str(i)
        url = 'https://m-bnmanhua-com.mipcdn.com/i/bnpic.comic123.net/upload/files/15127/'+d+'/'+b+'.jpg'
        print(url)
        response = requests.get(url).status_code
        if response ==200:
            req = urllib.request.Request(url)
            u = urllib.request.urlopen(req)
            data = u.read()
            with open("test" + b + ".jpg", 'wb') as f:
                f.write(data)
                sleep(0)
        else:
            i+=1



