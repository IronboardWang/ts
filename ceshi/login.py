# coding: utf-8


from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'tesst'
desired_caps['app'] = r'E:\app\wsgwApp\app\build\outputs\apk\debug\app-debug.apk'
desired_caps['appPackage'] = " com.example.lbstest"
desired_caps['appActivity'] = 'com.example.lbstest.ui.LoadingActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)
    ele = driver.find_element_by_id('com.example.lbstest:id/input_email')
    ele.send_keys('444')
    ele = driver.find_element_by_id('com.example.lbstest:id/input_password')
    ele.send_keys('444')
    driver.find_element_by_id(
        "com.example.lbstest:id/btn_login").click()
    time.sleep(1)
except: print("worong")
finally:print("finally")