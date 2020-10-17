"""
添加成员方式：手动输入添加
"""
# from appium_weixin_po.pages.contact_edit_page import ContactEditPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from appium_weixin_po.pages.base_page import BasePage


class MemberInvitePage(BasePage):
    _add_member = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    # 定义一个构造函数接收传递过来的drivr
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_manual(self):
        from appium_weixin_po.pages.contact_edit_page import ContactEditPage
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self._add_member)
        return ContactEditPage(self.driver)

    def get_toase(self):
        # mytoast = WebDriverWait(self.driver, 5).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")).text
        #定义一个变量存放BasePage中返回的text文本信息
        mytoast = self.get_toast_text()
        return mytoast