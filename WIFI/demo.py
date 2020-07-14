from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from pathlib import Path
import shutil


if __name__ == "__main__":
    browser = webdriver.Chrome()
    #driver = webdriver.PhantomJS()
    browser.get(url="https://www.douban.com")
    # id
    ret1 = browser.find_element_by_id("anony-nav")
    ret2 = browser.find_elements_by_id("anony-nav")
    # class name
    ret3 = browser.find_element_by_class_name("anony-srh")
    # Xpath
    ret4 = browser.find_element_by_xpath('//*[@id="anony-nav"]/h1/a')
    # 内容
    ret5 = browser.find_element_by_link_text("豆瓣")
    # 模糊内容
    ret6 = browser.find_elements_by_partial_link_text("豆瓣")
    # for ret in ret6:
    #     print(ret)
    # 通过标签名
    ret7 = browser.find_elements_by_tag_name("div")
    # 获取标签的文本内容
    ret8 = browser.find_element_by_tag_name("div")
    print(ret8.text)
    # 通关标签找到属性
    try:
        ret9 = browser.find_element_by_link_text("下载豆瓣 App")
    except NoSuchElementException:
        print("没有找到对象")
    else:
        print(ret9.get_attribute("href"))

    finally:
        sleep(5)
        browser.quit()
