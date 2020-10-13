"""
通讯录页面：
点击添加部门，弹出添加部门窗口
"""
from time import sleep

from selenium.webdriver.common.by import By

from weixin_selenium_po.pages.basepage import BasePage
from weixin_selenium_po.pages.create_department_page import CreateDepartment


class ContactPage(BasePage):
    # _定义为私有，元素不暴露给外部
    _add_btn = (By.CLASS_NAME, "member_colLeft_top_addBtn")
    _create_party = (By.CLASS_NAME, "js_create_party")
    _depart_list = (By.CSS_SELECTOR, ".jstree-anchor")

    def go_to_create_department(self):
        # 查找到+并点击
        self.find(*self._add_btn).click()
        # 找到添加部门并点击
        self.find(*self._create_party).click()
        return CreateDepartment(self.driver)

    # 获取部门列表方法，用于用例中断言
    def get_department_list(self):
        sleep(5)

        ele = self.finds(*self._depart_list)
        # 返回列表中的每个部门名称
        return [depart.text for depart in ele]
