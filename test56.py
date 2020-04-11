import matplotlib

from matplotlib import pyplot as pt
import numpy
import random
from matplotlib import font_manager
x = range(11,31)
y = [1,0,2,3,1,2,3,2,1,1,2,1,1,1,0,1,2,1,1,1]
y1 = [0,0,2,3,1,3,2,3,1,1,2,0,0,1,0,0,1,1,0,1]
pt.figure(figsize=(20,8),dpi=80)
"""font = {
    'family' :'MicroSoft YaHei',
    'weight' : 'bold',
    'size' : 'larger'
}
matplotlib.rc("font",**font)
matplotlib.rc("font",family = 'MicroSoft YaHei',weight ='bold',size ='larger')"""

pt.plot(x,y,label="me",linestyle='--',linewidth='3')
pt.plot(x,y1,label="you")
_x = ["{}".format(i) for i in x]
#_x = _x + ["11:{}".format(i) for i in range(60)]
pt.xticks(x,_x)
#pt.xticks(list(x)[::1],_x[::1])
pt.grid(alpha=0.2)
pt.legend()
pt.show()