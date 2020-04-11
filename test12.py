import requests
from requests.exceptions import  RequestException
import re
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)<\a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.s)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
        }
    print(items)
def main():
    url = 'https://maoyan.com/board/4?'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)

if __name__  == '__main__':
    main()