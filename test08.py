from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
def search():
    try:
       driver.get('https://www.tmall.com')
       input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mq'))
        )
       submit = wait.until( EC.element_to_be_clickable((By.CSS_SELECTOR,'#mallSearch > form > fieldset > div > button')))
       input.send_keys('手机')
       submit.click()
       total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div > div.ui-page > div > b.ui-page-skip > form > input[type=hidden]:nth-child(5)')))
       print(total)
       return total.text
    except TimeoutException:
        return search()
def main():
    total = search()
    print(total)
if __name__ == '__main__':
    main()