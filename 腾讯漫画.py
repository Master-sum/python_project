import requests

def one_page():
    url = 'https://ac.qq.com/ComicView/index/id/644506/cid/2'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print(response.text)
one_page()