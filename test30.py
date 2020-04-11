import requests
import re
def one_page():
    response = requests.get("https://www.9dxs.com/0/410/11128837.html")
    response.encoding='gbk'
    title = re.findall(r'<h1>章节目录 (.*?)</h1>',response.text)[0].strip()
    content = re.findall(r'<p>(.*?)</p>',response.text,re.S)[0].strip()
    content = content.replace('&nbsp;','')
    content = content.replace('<br />','')
    with open('%s.txt'%title,'w',encoding='utf-8') as f:
        f.write('%s\n'%title)
        f.write('%s\n'%content)