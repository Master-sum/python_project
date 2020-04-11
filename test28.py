from bs4 import BeautifulSoup
from lxml import etree
import lxml
import re
import urllib.request
url='https://movie.douban.com/top250?start='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'lxml')
s = soup.xpath("//div[@class='item']//a/span[@class='title']/text()").extract()[0]
print(s)