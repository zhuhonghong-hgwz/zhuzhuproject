"""
添加部门页面
"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from weixin_selenium_po.pages.basepage import BasePage


class CreateDepartment(BasePage):
    _input_text = (By.CSS_SELECTOR, ".member_tag_dialog_inputDlg .ww_inputText")
    _dropdown_btn = (By.CSS_SELECTOR, ".js_toggle_party_list .ww_btn_Dropdown_arrow")
    _depart_container = (By.CSS_SELECTOR, ".js_party_list_container .jstree-anchor")
    _commit_btn = (By.CSS_SELECTOR, ".ww_dialog_foot .ww_btn_Blue")

    def create_department(self, depart_name):
        # 找到添加部门输入框,并输入部门名称
        self.find(*self._input_text).send_keys(depart_name)
        # 找到下拉箭头，并点击
        self.find(*self._dropdown_btn).click()
        # 找到所属部门，并点击
        self.find(*self._depart_container).click()
        return self

    # 定义一个点击确认按钮的方法
    def save_department(self):
        from weixin_selenium_po.pages.contact_page import ContactPage
        # 找到确定按钮，并点击
        self.find(*self._commit_btn).click()
        # 保存后返回通讯录页面
        return ContactPage(self.driver)

    # 定义一个点击取消按钮的方法
    def cancel_department(self):
        from weixin_selenium_po.pages.contact_page import ContactPage
        # 定位取消按钮,并点击
        self.find(By.CSS_SELECTOR, ".ww_dialog_foot a:nth-child(2)").click()
        # 点击取消后返回通讯录页面
        return ContactPage(self.driver)
