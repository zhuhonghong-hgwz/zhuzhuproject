"""
通讯录页面：
添加成员
搜索联系人
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.pages.base_page import BasePage
from appium_weixin_po.pages.member_invite_page import MemberInvitePage
from appium_weixin_po.pages.search_member_page import SearchMemberPage


class AddressListPage(BasePage):
    _add_member_ele = "添加成员"
    _search_member_ele = (MobileBy.ID, "com.tencent.wework:id/hvn")
    # 定义一个构造函数接收传递过来的drivr
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self._add_member_ele)
        return MemberInvitePage(self.driver)

    def goto_search_member(self):
        #查找定位图标并点击
        self.find_and_click(self._search_member_ele)
        return SearchMemberPage(self.driver)
