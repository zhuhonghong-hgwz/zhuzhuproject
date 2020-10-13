"""
企业微信主页面:
点击通讯录进入通讯录界面
"""
from selenium.webdriver.common.by import By

from weixin_selenium_po.pages.basepage import BasePage
from weixin_selenium_po.pages.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _menu_contacts = (By.ID, "menu_contacts")

    def go_to_contact(self):
        # 查找通讯录并点击
        self.find(*self._menu_contacts).click()
        return ContactPage(self.driver)
