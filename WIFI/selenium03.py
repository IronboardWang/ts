from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

if __name__ == "__main__":
    browser = webdriver.Chrome()
    #driver = webdriver.PhantomJS()
    browser.get(url="https://www.douban.com")
    # 如何切换窗口
    try:
        movie_but = browser.find_element_by_xpath(
            '//*[@id="anony-nav"]/div[1]/ul/li[2]/a')
    except NoSuchElementException:
        print("没有找到对象")
    movie_but.click()

    # 1获取当前所有窗口
    current_windows = browser.window_handles
    print(type(current_windows))

    # 2 switch切换
    browser._switch_to.window(current_windows[0])
    sleep(2)
    browser._switch_to.window(current_windows[1])
    select_movies = browser.find_element_by_partial_link_text("选电影")
    select_movies.click()
    sleep(1)

    # 3 頁面的前進與後退
    browser.back()
    browser.forward()



    # sleep(2)
    # browser.quit()
