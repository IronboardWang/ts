from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

if __name__ == "__main__":
    driver = webdriver.Chrome()
    #driver = webdriver.PhantomJS()
    driver.get(url="https://www.douban.com")
# 4 switch进入嵌套网页
    driver.switch_to.frame(0)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/ul[1]/li[2]').click()
    user = driver.find_element_by_id("username")
    user.send_keys(13623472610)
    pw = driver.find_element_by_id("password")
    pw.send_keys("wang1127878660")
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
