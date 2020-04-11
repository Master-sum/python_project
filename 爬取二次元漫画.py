from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,requests,time,os



#获取爬取的url
def get_url():
    all_url =[]
    id = [107977,110175,110184,110195,110206,110215,110224,110235,110243,110252,110262,110270,110279,110288,110296,110305,110316]
    for i in range(0,16):
        for j in range(1,35):
            start_url = "https://www.2animx.com/index-look-name-%E9%87%91%E7%93%B6%E6%A2%85-cid-16928-id-{}-p-{}".format(id[i],j)
            meta = re.compile(r"content=\"https://img.2animx.com/(\S+)\"")
            try:
                html = urlopen(start_url,timeout=20)
                bs = BeautifulSoup(html,'html.parser')
                jpg_url = meta.findall(str(bs))
                lata_url = jpg_url[0]
                print(lata_url)
            except Exception as f:
                print(f)
            #获取图片
            time.sleep(2)
            path1 = r"F:\{}".format(i+16)
            isExists = os.path.exists(path1)
            if not isExists:
                os.makedirs(path1)
                print(1)
            else:
                print(2)
            path = r"{}\{}.JPG".format(path1,j)
            try:
                b1 = requests.get(lata_url, timeout=20)
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

    return all_url
'''
def save_p(all_url):
    a = 2
    for url in all_url:

        time.sleep(2)
        name = re.compile(r"https://img.2animx.com/upload/img/1w/69b/16928/1/(\S+).JPG")
        page_name = name.findall(url)
        print(page_name)
        path1 = r"F:\{}".format(a)
        isExists = os.path.exists(path1)
        if not isExists:
            os.makedirs(path1)
            print(1)
        else:
            print(2)
        path = r"{}\{}.JPG".format(path1, name[0])
        try:
            b1 = requests.get(url,timeout=20)
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
'''
a = get_url()
