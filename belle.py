from bs4 import BeautifulSoup
from urllib.request import urlopen
import re,requests,os,time,sys
html = urlopen('http://666renti.com/mn/TuiGirl/0709/1104.html')
r = r'(http://\S+\.jpg)'
soup = BeautifulSoup(html,'html.parser')
p = re.compile(r)
url = 'https://tp.85814.com/d/file/shutu/2018-05/20150301093745255.jpg!800'
path = r"f:\belle\%s.jpg"%1
print("wqwq")
headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

img1 = requests.get(url,headers=headers)
print("222")
print(img1.status_code)
with open(path, 'wb') as f:
    f.write(img1.content)
    f.close()


