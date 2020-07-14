from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import sleep
import pprint

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '9',  # 手机安卓版本
    'deviceName': 'wang',  # 设备名，安卓手机可以随意填写（主要是苹果用）
    # 自动化应用的包名
    'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称
    'appActivity': '.ui.splash.SplashActivity',  # 启动Activity名称

    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,       # 不要重置App，建议加上，如果不加，则为刚安装上的app
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
    # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements_by_id("text3")
if iknow:
    iknow.click()
# 下拉通知栏
# driver.open_notifications()
# sleep(2)
# driver.press_keycode(AndroidKey.BACK)

# # 向左滑动
# l = driver.get_window_size()
# x1 = l['width'] * 0.9
# y1 = l['height'] * 0.5
# x2 = l['width'] * 0.5
# # 向左滑动
# driver.swipe(x1,y1,x2,y1,200)
# print('已经向左滑动了')
# sleep(1)
# sleep(1)
# # 下滑
# l=driver.get_window_size()
# x1 = (l['width'] * 0.5)
# y1 = (l['height'] * 0.9)
# y2 = (l['height'] * 0.35)
# driver.swipe(x1, y1, x1, y2, 1000)
# sleep(1)
# print('已经向xia滑动了')
# 根据id定位搜索位置框，点击
# driver.find_element_by_id("expand_search").click()
# driver.back()
# 根据id定位搜索输入框，点击
# sbox = driver.find_element_by_id('search_src_text')
# sbox.send_keys('白月黑羽')

# 输入回车键，确定搜索
# driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
# eles = driver.find_elements_by_class_name("android.widget.TextView")
#
# for ele in eles:
#     # 打印标题
#     print(ele.text)

# 使用  uiautomator
driver.find_element_by_id("expand_search").click()
sbox = driver.find_element_by_id('search_src_text')
sbox.send_keys("华农")
driver.press_keycode(AndroidKey.ENTER)
# code = 'new UiSelector().textContains("华农").className("android.widget.TextView").instance(4)'
# ele = driver.find_element_by_android_uiautomator(code)
# print(ele)
sleep(2)
code = 'new UiSelector().text("华农兄弟：去兄弟家恰饭，给他带了点小礼物，看他笑的多开心").resourceId("tv.danmaku.bili:id/title")'
ele = driver.find_element_by_android_uiautomator(code)
ele.click()
sleep(1)
driver.press_keycode(AndroidKey.BACK)
sleep(1)
#input('**** Press to quit..')
driver.quit()
