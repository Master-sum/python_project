from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml
from lxml import etree
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

url_all ={}
for j in range(0,100):
    if j < 1:
        html = urlopen('https://www.xsnvshen.com/girl/t79/')
        bs = BeautifulSoup(html, 'html.parser')
        page = bs.ul.find_all('img', src=re.compile(r"//(\S+).jpg"))
        for i in page:
            n = re.compile(r"alt=\"(\S+)\"")
            sr = re.compile(r"src=\"(\S+).jpg")
            name = n.findall(str(i))
            src = sr.findall(str(i))
            belle_name = "".join(name)
            belle_src = "".join(src)
            late = re.compile(r"//img.xsnvshen.com/thumb_205x308/album/(\d{5})")
            lat_src = late.findall(belle_src)
            late_src = "https://www.xsnvshen.com/girl/"+"".join(lat_src)
            url_all[belle_name] = str(late_src)

    else:
        html = urlopen('https://www.xsnvshen.com/girl/t79/?p=%d'%j)
        bs = BeautifulSoup(html, 'html.parser')
        page = bs.ul.find_all('img', src=re.compile(r"//(\S+).jpg"))
        for i in page:
            n = re.compile(r"alt=\"(\S+)\"")
            sr = re.compile(r"src=\"(\S+).jpg")
            name = n.findall(str(i))
            src = sr.findall(str(i))
            belle_name = "".join(name)
            belle_src = "".join(src)
            late = re.compile(r"//img.xsnvshen.com/thumb_205x308/album/(\d{5})")
            lat_src = late.findall(belle_src)
            late_src = "https://www.xsnvshen.com/girl/" + "".join(lat_src)
            url_all[belle_name] = str(late_src)
print(url_all)

def person_all(url_all):

    for key in url_all:
        time.sleep(3)
        print(key,url_all[key])
        html = urlopen(str(url_all[key]))
        bs = BeautifulSoup(html, 'html.parser')
        page = bs.find_all('img', src=re.compile(r"//img.xsnvshen.com/thumb_205x308/album/(\S+)/cover.jpg"))
        for pagelink in page:
            print(89282002)
            print(pagelink)
            n = re.compile(r"(\S+)")
            sr = re.compile(r"src=\"//img.xsnvshen.com/thumb_205x308/album/(\S+)/cover.jpg")
            file = re.compile(r"src=\"//img.xsnvshen.com/thumb_205x308/album/\d+/(\S+)/cover.jpg")
            name = n.findall(str(pagelink))
            src = sr.findall(str(pagelink))
            file_n = file.findall(str(pagelink))
            alt_name = "".join(name)
            dat_src = "".join(src)
            file_name = "".join(file_n)
            print(alt_name,dat_src)
            time.sleep(3)
            URL='https://www.xsnvshen.com/album/'+'%s'%file_name

            html1 = urlopen(URL)
            bs1 = BeautifulSoup(html1,'html.parser')
            num1 = re.compile(r"共 (\d+) 张")

            num1_page = num1.findall(str(bs1.em.span))
            print(num1_page)
            num1_page_all = num1_page[0]
            print(num1_page_all)
            for b in range(0, int(num1_page_all)):
                print(b)
                header_t = random.choice(my_headers)

                headers = {
                    "Referer": "https://www.xsnvshen.com/album/%s"%dat_src,
                    "Sec-Fetch-Dest": "image",
                    "Upgrade-Insecure-Requests": "%d" % b,
                    "User-Agent": "%s" % header_t
                }

                time.sleep(5)
                if b < 10:
                    url = 'https://img.xsnvshen.com/album/{}/00{}.jpg'.format(dat_src,b)
                else:
                    url = 'https://img.xsnvshen.com/album/{}/0{}.jpg' .format(dat_src,b)
                print(url)
                path = r"f:\belle\%s+%s.jpg" % (file_name,b)
                try:
                    b1 = requests.get(url, headers=headers, timeout=20)
                    print(b1)
                    print("222")
                    print(b1.status_code)
                    with open(path, 'wb') as f:
                        f.write(b1.content)
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

        print(1111111111111111)

person_all(url_all)