from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'LNHIQ8V899999999'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.main.MainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(20)
driver.find_element_by_id('com.ss.android.ugc.aweme:id/c_3').click()
time.sleep(5)
driver.find_element_by_id('com.ss.android.ugc.aweme:id/b2g').click()
for i in range(30):
    x = driver.get_window_size()['width']  # 获取屏幕x大小
    y = driver.get_window_size()['height']  # 获取屏幕y大小
    x1 = int(x * 0.5)  # x坐标
    y1 = int(y * 0.75)  # 起始y坐标
    y2 = int(y * 0.15)  # 终点y坐标

    driver.swipe(x1, y1, x1, y2, 7000)
print(x1)
time.sleep(10)

