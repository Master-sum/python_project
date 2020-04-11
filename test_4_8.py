from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,ssl,requests,time,urllib,random
ssl._create_default_https_context = ssl._create_unverified_context

my_headers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
start=["//img.xsnvshen.com/album/20946/23797/001.jpg"]

for i in range(0, 22):
    header_t = random.choice(my_headers)

    headers = {
        "Referer": "https://www.xsnvshen.com/album/23860",
        "Sec-Fetch-Dest": "image",
        "Upgrade-Insecure-Requests": "%d"%i,
        "User-Agent": "%s"%header_t
    }
    proxie = {
        "http":"104.24.120.235:443",
        "http": "36.248.129.205:9999",
        "http": "183.166.102.205:9999",
        "http": "119.254.94.93:44665",
        "https":"117.88.176.110:3000",
        "https": "223.245.45.162:65309",
        "https": "113.66.6.254:808",
        "https": "223.241.119.14:8010",
    }
    time.sleep(5)
    if i<10:
        url = 'https://img.xsnvshen.com/album/17198/17178/00%d.jpg'%i
    else:
        url = 'https://img.xsnvshen.com/album/17198/17178/0%d.jpg' % i
    print(url)
    path = r"f:\belle\1+%s.jpg" % (i)
    try:
        b = requests.get(url, headers=headers,timeout=20)
        print(b)
        print("222")
        print(b.status_code)
        with open(path, 'wb') as f:
            f.write(b.content)
            f.close()

    except requests.HTTPError as f:
        print(f)

    except Exception as e:
        print(e)

    except requests.exceptions.Timeout:
        print("失败")
        time.sleep(10)
    except Exception as f:
        print("超时" + str(f))

