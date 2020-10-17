"""
app首页:通讯录和工作台
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.pages.addresslist_page import AddressListPage
from appium_weixin_po.pages.base_page import BasePage


class MainPage(BasePage):
    #定义私有元素，传递给封装的find方法
    _contact_ele = (MobileBy.XPATH, "//*[@text='通讯录']")
    #定义一个构造函数接收传递过来的drivr
    # def __init__(self, driver):
    #     self.driver = driver

    #跳转到通讯录页面
    def goto_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click(self._contact_ele)
        return AddressListPage(self.driver)

    def goto_workbench(self):
        pass
