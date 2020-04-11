from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,time,requests
import ssl
a = []
ssl._create_default_https_context = ssl._create_unverified_context
headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
url = "https://m.girlsky.cn/tag_rentiyishuzhao.html"
d = [11798,11222,11256,10972,10794,10860,8500,8888,8298]
for j in range(11):
    for i in range(34):
        path = r"f:\belle\%s+%s.jpg" % (j,i)
        time.sleep(3)
        if i >=1:
            url = "http://m.girlsky.cn/article/%d/%d/index.html" % (d[j],i+1)

            html = urlopen(url)
            bs = BeautifulSoup(html.read(), 'html.parser')
            img = re.findall(r"(http://\S+\.jpg|http://\S+\.gif)", str(bs.img))
            print(bs.img)
            if img != []:
                print(img)
                i = requests.get(img[0], headers=headers)
                print("222")
                print(i.status_code)
                with open(path, 'wb') as f:
                    f.write(i.content)
                    f.close()


        else:
            i += 1
