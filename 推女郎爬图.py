from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,ssl
ssl._create_default_https_context = ssl._create_unverified_context
data = {
    "Sec-Fetch-Dest":"image",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
start_url = "https://www.xsnvshen.com/album/"
html = urlopen(start_url,timeout=20)
bs = BeautifulSoup(html,'html.parser')
print(bs.ul)

"https://img.xsnvshen.com/album/24960/23860/005.jpg"