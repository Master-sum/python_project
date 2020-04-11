from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getlinks(pageurl):
    global pages
    print(pageurl)
    html = urlopen('https://www.iqiyi.com{}'.format(pageurl))
    bs = BeautifulSoup(html,'html.parser')

    for link in bs.find_all('a',href = re.compile('(/dianshiju/)')):
        if 'href' in link.attrs:
            newpage = link.attrs['href']
            if '.iqiyi.' in str(newpage):
               a = re.findall(r'//www.iqiyi.com(.*?)',newpage)
               print(a)
            '''
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getlinks(newpage)
                '''
if __name__ == '__main__':

    getlinks('')