import re
s = "//www.iqiyi.com\
//www.iqiyi.com/dianshiju/\
//www.iqiyi.com/dianying/\
//www.iqiyi.com/zongyi/\
//www.iqiyi.com/dongman/"


a = re.compile(r'dianshiju')
b = a.findall(s)
print(b)