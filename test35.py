from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1：62001'
desired_caps['appPackage'] = 'com.taobao.taobao'
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(10)
driver.find_element_by_id('com.taobao.taobao:id/welcom_dialog_checkbox').click()
driver.find_element_by_id('com.taobao.taobao:id/uik_mdButtonDefaultPositive').click()
#点击同意界面
time.sleep(5)
print('---------')
driver.find_element_by_id('com.taobao.taobao:id/provision_positive_button').click()
#进入主界面
time.sleep(5)

'''
driver.find_element_by_id('com.zkteco.zkbiosecurity.pro:id/login_username_et').send_keys(24)
driver.find_element_by_id('com.zkteco.zkbiosecurity.pro:id/login_password_et').send_keys(123456)
#driver.find_element_by_id('com.zkteco.zkbiosecurity.pro:id/login_register_tv').click()
time.sleep(1)
driver.find_element_by_id('com.zkteco.zkbiosecurity.pro:id/login_register_tv').click()
'''
while True:
   driver.find_element_by_id('com.zkteco.zkbiosecurity.pro:id/login_register_tv')
   print('ee')
'''
time.sleep(3)
driver.find_element_by_id('com.zkteco.zkbiosecurity.pro:id/register_btn').click()
while True:
   TouchAction(driver).tap(x=546, y=1748).perform()
   print("输入信息")
   driver.quit()
   '''