import re
str ="//img.xsnvshen.com/thumb_205x308/album/22162/22162"

late = re.compile(r"//img.xsnvshen.com/thumb_205x308/album/(\d{5})")
late_src =late.findall(str)
print(late_src)
