from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl,re,requests,time
import urllib.error
ssl._create_default_https_context = ssl._create_unverified_context

headers ={
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
def Url_all():
    try:
        start_url = "https://www.39um.com/yzrt/"
        html = urlopen(start_url)
        bs = BeautifulSoup(html.read(), 'html.parser', from_encoding='gb2312')
        page = bs.find_all('a', href=re.compile(r"(\d+.html)"))
        print(page)
        b = []
        for i in page:
            print(str(i))
            a = re.compile(r"href=.(\S+).html")
            t = a.findall(str(i))
            b.append(t[0])
            print(t)
        print(b)
    except Exception as e:
        print("url_all超时"+str(e))
        return Url_all
    return b
def url_func(b):
    url = []
    print(2121)
    for i in range(10):
        if i<1:
            start_url = "https://www.39um.com/yzrt/"
            try:
                html = urlopen(start_url)
                bs = BeautifulSoup(html.read(), 'html.parser',from_encoding='gb2312')
                imglink = bs.findAll('a',{'href':re.compile(r"(/yzrt/\d+)")})
            except Exception as e:
                return url_func
                print("第一次"+str(e))
            for img in imglink:
                url.append(img['href'])
        else:
            print(b[i-1])
            start_url = "https://www.39um.com/yzrt/"+b[i-1]
            html = urlopen(start_url)
            bs = BeautifulSoup(html.read(), 'html.parser', from_encoding='gb2312')
            try:
                html = urlopen(start_url)
                bs = BeautifulSoup(html.read(), 'html.parser', from_encoding='gb2312')
                imglink = bs.findAll('a', {'href': re.compile(r"(/yzrt/\d+)")})
            except Exception as e:
                return url_func
                print("第一次" + str(e))
            for img in imglink:
                url.append(img['href'])

    return url

def get(url):
    print(211)
    print(url)
    for urllink in url:
        print(urllink)
        t_b = re.findall("\d+", urllink)
        t_b_n = str(t_b[0])
        print(t_b)
        print(t_b_n)
        use = "https://www.39um.com"+urllink
        try:
            html = urlopen(use,timeout=20)
            bs = BeautifulSoup(html.read(), 'html.parser')
            page = bs.findAll('a',{'href':re.compile(r"(\d+.html)")})
            num_all = []
            for num in page:
                num_page = num['href']
                num_one = re.findall("\d+", num_page)
                num_all.append(num_one)
            late = num_all[-1]
            b = late[0]
            c = int(b) + 1
        except Exception as f:
            print("chashi"+str(f))
        time.sleep(3)
        #img = re.findall(r"(http://\S+\.jpg|http://\S+\.gif)", str(bs.img))
        print(c)
        for i in range(c):
            if i > 1:
                end_url = use + '%s.html' % i
                path = r"f:\belle\%s+%s.jpg" % (t_b_n,i)
                try:
                    print(2121121)
                    html = urlopen(end_url, timeout=10)
                    bs = BeautifulSoup(html.read(), 'html.parser')
                    img = re.findall(r"(https://\S+\.jpg|https://\S+\.gif)", str(bs))
                    print(212)
                    print(img)
                    if img != []:
                        print(img)
                        try:
                            i = requests.get(img[0], headers=headers, timeout=20)
                            print("222")
                            print(i.status_code)
                            with open(path, 'wb') as f:
                                f.write(i.content)
                                f.close()
                        except requests.HTTPError as f:
                            print(f)

                        except Exception as e:
                            print(e)

                        except requests.exceptions.Timeout:
                            print("失败")
                            time.sleep(10)
                except Exception as f:
                    print("超时"+str(f))
            else:
                i += 1
    print(url)
if __name__ =="__main__":
    b = Url_all()
    print(b)
    a = url_func(b)
    get(a)