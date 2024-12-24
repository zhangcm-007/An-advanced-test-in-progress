from selenium.webdriver.support import expected_conditions as EC

from appium.options.common import AppiumOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


def test_xueqiu_search():
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
    driver.find_element(by=AppiumBy.XPATH,value="//*[@text='基金']/../preceding-sibling::*[2]").click()
    driver.find_element(by=AppiumBy.XPATH,value='//*[@class="android.widget.ImageButton"]').click()
    #查询搜索输入框，输入招商银行，进行搜索并断言
    input_box = driver.find_element(by=AppiumBy.XPATH,value='//*[@text="搜索"]/../../../../../preceding-sibling::*[1]')
    input_box.click()
    input_box.send_keys("招商银行")
    tips = driver.find_elements(AppiumBy.XPATH,'//*[@text="搜索"]/../../../../../../../following-sibling::*[1]/*/*/*/*')
    # name_list = []
    # for i in tips:
    #     # 获取每个父元素下的所有儿子元素（假设通过某种方式可以定位这些儿子元素）
    #     children = i.find_elements(AppiumBy.XPATH, "./*")  # 获取所有儿子元素
    #     print(children)
    #
    #     for ii in children:
    #         # 获取儿子的儿子
    #         print('ii*******', ii)
    #         # grandchildren = ii.find_elements(AppiumBy.XPATH, "./*")  # 获取孙子元素
    #         # #第二个儿子
    #         # print('*******',grandchildren)
    #         # grandchildren2 = grandchildren[1]
    #         #
    #         # # 检查是否有至少一个孙子元素
    #         # if grandchildren2:
    #         #     # 获取第一个孙子元素的所有儿子元素
    #         #     first_grandchild_children = grandchildren[0].find_elements(AppiumBy.XPATH, "./*")
    #         #
    #         #     # 如果第一个孙子有儿子元素，则获取第一个儿子的 text
    #         #     if first_grandchild_children:
    #         #         name_list.append(first_grandchild_children[0].text)
    # assert "招商银行" in name_list

def test_add_optional():
    #加自选，断言toast提示
    options = AppiumOptions()
    options.load_capabilities({"platformName": "android",
                               "appium:automationName": "uiautomator2",
                               "appium:deviceName": "12",
                               "appium:appPackage": "com.xueqiu.android",
                               "appium:appActivity": ".view.WelcomeActivityAlias",
                               "appium:noReset": True,
                               "appium:forceAppLaunch": True})  # 是否强制重启

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    # 隐式等待
    driver.implicitly_wait(5)
    driver.find_element(by=AppiumBy.XPATH, value="//*[@text='基金']/../preceding-sibling::*[2]").click()
    driver.find_element(by=AppiumBy.XPATH,value='//*[@text="市场情报站"]/../following-sibling::*[2]/*[1]/*[1]/*[2]').click()
    toast_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//*[@class='android.widget.Toast']"))
    )


    assert toast_message == '已删除自选'

    #已删除自选
