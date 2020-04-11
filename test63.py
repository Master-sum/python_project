import re
s="i love you not because 12sd 34er 56df e4 54434"
b = r'\b([0-9]+[a-z]{0,9})'#匹配以数字开头的单词
#开始匹配空格（提取内容）匹配数字+匹配存在字符
#第二种
c = r'\b(\d+)'
a = re.findall(c,s)

print(a)