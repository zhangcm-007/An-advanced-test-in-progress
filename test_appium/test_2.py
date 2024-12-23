from appium.options.common import AppiumOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


def test_xueqiu():
    options =AppiumOptions()
    options.load_capabilities({"platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:deviceName": "12",
    "appium:appPackage": "com.xueqiu.android",
    "appium:appActivity": ".view.WelcomeActivityAlias",
    "appium:noReset": True,
    "appium:forceAppLaunch":True}) #是否强制重启


    driver = webdriver.Remote("http://127.0.0.1:4723",options = options)
    #隐式等待
    driver.implicitly_wait(5)
    driver.find_element(by=AppiumBy.XPATH,value="//*[@text='雪球']/../following-sibling::*[1]").click()
    driver.find_element(by=AppiumBy.XPATH,value='//*[@class="android.widget.ImageButton"]').click()
