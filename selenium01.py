from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_class_name('s_ipt').send_keys('80s')
driver.find_element_by_id('su').click()
driver.back()
time.sleep(3)




