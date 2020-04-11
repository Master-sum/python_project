import requests
import json
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=jQuery34108391163145268212_1580293247693&_=1580293247700'
headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'}
res = requests.get(url, headers=headers).text
a = res.split('jQuery34108391163145268212_1580293247693(')[1].split(')')[0]
c = json.loads(a)
ass = json.loads(c['data'])
path = str(input('请输入你需要查找的地区：'))
num = -1
for i in ass:
    num += 1
    if path == i['city']:
        print('地区：' + str(ass[num]['city']))
        print('确诊：' + str(ass[num]['confirm']))
        print('死亡：' + str(ass[num]['dead']))
        print('治愈：' + str(ass[num]['heal']))
