from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(10)
driver.get(url="http://www.baidu.com/")
try:
    # CSS选择器
    ele = driver.find_element_by_id("kw")
except NoSuchElementException:
    print("meiyou")
sleep(2)
ele.send_keys("东北林业大学")
sleep(2)

driver.find_element_by_id("su").click()

# current_windows = driver.window_handles
# driver._switch_to.window(current_windows[0])
# driver.close()
# sleep(2)


# 选择框
#radio/checkbox
#checkbox 可以先都取消，之后选择自己想要的 先选中之后用for
driver.find_elements_by_css_selector("#raido input[value='xxx']").click()
#select sel有专门的类
select = Select(driver.find_element_by_id("ss"))
select.select_by_visible_text("")# 选择
select.deselect_by_visible_text("") #去选

#更多动作ActionChain

# 弹窗
#ok
driver.switch_to_alert.accept()
#文本
print(driver.switch_to_alert.text)
#cancel
driver.switch_to_alert.dismiss()
#输入文本
driver.switch_to_alert.send_keys("")
driver.quit()
