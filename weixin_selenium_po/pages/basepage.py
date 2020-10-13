"""
封装公共方法
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _base_url = ""

    # 所有继承BasePage的子类都会执行这个构造函数
    def __init__(self, driver_base=None):
        # 只有driver为空时才需要进行初始化，否则使用已有的driver
        if driver_base is None:
            # 复用已打开的浏览器
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # 打开页面.和业务相关应该放在Page层面
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            # WebDriver注解，为了其他文件中可以使用self.driver
            self.driver: WebDriver = driver_base
        if self._base_url != "":
            self.driver.get(self._base_url)
        # 加入隐式等待，解决找不到元素的问题
        self.driver.implicitly_wait(5)

    # 定义显示等待方法
    def wait_for_clickable(self, element):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))

    # 封装find_element的方法
    def find(self, by, value):
        return self.driver.find_element(by, value)

    #封装find_elements的方法
    def finds(self, by, value):
        return self.driver.find_elements(by, value)