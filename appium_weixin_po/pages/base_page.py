"""
BasePage基类
封装最基本的公共方法： find, find_and_click(), find_and_get_text，find_and_send_keys(), webdriverwait, gettoast_text …
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 公共初始化方法
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 封装find方法,传入一个查找元素的元组参数
    def find(self, locator):
        # 对传入的元组参数进行解包，并返回查找到的值
        return self.driver.find_element(*locator)

    # 封装find_and_click方法,传入一个查找元素的元组参数
    def find_and_click(self, locator):
        # 调用find方法时进行解包
        self.find(locator).click()

    # 封装find_and_send_keys方法
    def find_and_send_keys(self, locator, value):
        self.find(locator).send_keys(value)

    # 封装滚动查找点击方法
    def find_by_scroll_and_click(self, text):
        locator = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find_and_click(locator)

    # 封装查找并获取toast文本信息的方法
    def find_and_get_text(self, locator):
        # 返回获取到的text文本信息
        return self.find(locator).text

    # 封装get toast方法
    def get_toast_text(self):
        toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        return self.find_and_get_text(toast_ele)

    # 封装find_elements方法
    def finds(self, name):
        locator = (MobileBy.XPATH, f"//*[@text='{name}']")
        return self.driver.find_elements(*locator)

    # 封装显示等待元素出现的方法
    def wait(self, element):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(element))
