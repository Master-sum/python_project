import urllib

import requests
import re
import time
from bs4 import BeautifulSoup
import http.cookiejar
def get_nov_chapter():
    url='https://www.9dxs.com/0/410/index.html'
    headers = {
                  "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3",
                   "Accept-Language" : "zh-CN,zh;q=0.9",
                   "Referer": "https://www.9dxs.com/0/410/"
    }
    cjar = http.cookiejar.CookieJar()
    proxy = urllib.request.ProxyHandler({'http': "127.0.0.1:8888"})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))

    headall = []
    opener.addheaders = headall
    urllib.request.install_opener(opener)
    r = urllib.request.urlopen(url).read()


    soup = BeautifulSoup(r,"html.parser")
    data=[]
    i = -12
    for li in soup.find_all("li"):

        i += 1
        link = li.find("a")
        if not link:
            continue
        a = re.match(r'\d{2}',link['href'])
        if a != None:
           b = link['href']
           s = str(b)
          # print(b)

           data.append(("https://www.9dxs.com/0/410/" + b, link.get_text()))
           url = "https://www.9dxs.com/0/410/" + b
           print(url)
           response = requests.get(url)
           response.encoding = 'gbk'
           title = re.findall(r'<h1>章节目录 (.*?)</h1>', response.text)[0].strip()

           content = re.findall(r'<p>(.*?)</p>', response.text, re.S)[0].strip()
           content = content.replace('&nbsp;', '')
           content = content.replace('<br />', '')
           with open('%s.txt' % title, 'w', encoding='utf-8') as f:
               f.write('%s' % title)
               f.write('%s\n' % content)
               time.sleep(1)
               f.close()
               print(title)

get_nov_chapter()




