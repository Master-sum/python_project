from  selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
from selenium.webdriver.common.by import By

class Lagou:
    def __init__(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        #最大窗口
        self.driver.maximize_window()
        #初始化网站
        self.url = "https://www.lagou.com/"
        #head

    #打开页面
    def search(self,key1):
        self.driver.get(self.url)
        #搜索关键字
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class = 'tab focus']").click()
        #输入关键字
        self.driver.find_element_by_id("search_input").send_keys(key1)
        #关闭弹窗

        #点击搜索
        self.driver.find_element_by_id("search_button").click()
        #等待两秒
        time.sleep(2)
        self.driver.refresh()
        self.driver.find_element_by_xpath("//div[@class = 'body-btn']").click()

    #获取资源
    def source(self):
        self.driver.refresh()
        cur_page_source = self.driver.page_source
        # 总页数
        max_page_num = int(
            self.driver.find_element(By.XPATH, "//span[contains(@hidefocus, 'hidefocus')][last()-1]").text)
        for page in range(1, max_page_num):
            #调用解析函数
            self.get_page(cur_page_source)
            # 爬取当前页， 点击下一页进行抓取
            self.driver.find_element(By.CSS_SELECTOR, "div.pager_container .pager_next").click()

            # 防止被识别， 设置随机等待秒数
            rand_seconds = random.choice([2, 3]) + random.random()
            time.sleep(rand_seconds)
            cur_page_source = self.driver.page_source


    #解析页面
    def get_page(self,cur_page_source):
        #使用Beautiful解析界面
        soup = BeautifulSoup(cur_page_source,'lxml')
        #获取单条信息
        home_list = soup.select('.con_list_item')
        for item in home_list:
            d = dict()
            d['job'] = item.select_one(".position_link > h3").get_text()
            d['company'] = item.select_one(".company_name > a").get_text()
            d['salary'] = item.select_one(".money").get_text()
            print(d)

if __name__ == "__main__":
    hot = Lagou()
    page = hot.search('python')
    source_list = hot.source()
    hot.get_page()