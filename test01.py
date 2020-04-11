import requests
import time
from parsel import Selector
from urllib.error import URLError, HTTPError
def download_one(url):
    response = requests.get(url,timeout=40)
    response.raise_for_status()
    response.encoding="gbk"
    sel=Selector(response.text)
    title=sel.css('em::text').get()
    f=open(title+'.txt',mode='w',encoding='gbk')
    f.write(title)
    for list in sel.css('#content::text').getall():
        print(list.strip(),file=f)
    f.close()
response = requests.get('https://www.i7wx.com/book/10/10608/index.html')
response.encoding="gbk"
sel=Selector(response.text)
index=sel.css('#readerlist a::attr(href)').getall()

for list in index:
    list1=str(list)
    def getone():
        n=0
        while True:
            try:
                download_one('https://www.i7wx.com/book/10/10608/' + list1)
                n=0
            except Exception:
                list1.close()

                n+=1
                if n>5:
                    print('请求失败')
                    n=0
                    time.sleep(30)
                else:
                    print('123')
                    time.sleep(3)

    getone()
    continue
getone()










