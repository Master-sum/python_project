from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree
html = urlopen("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3")
obj = BeautifulSoup(html.read(),'html.parser')
#result = obj.xpath('html/body/div//section/a/text()')
print(obj)