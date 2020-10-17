"""
个人信息页面:
跳转到编辑成员页面

"""
from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.pages.base_page import BasePage
from appium_weixin_po.pages.edit_member_page import EditMemberPage


class PersonalInfoPage(BasePage):
    _detail_ele = (MobileBy.ID, "com.tencent.wework:id/hvd")
    _edit_member_ele = (MobileBy.ID, "com.tencent.wework:id/b87")

    # 跳转到编辑成员页面功能
    def go_to_edit_member(self):
        # 找到右上角的三个点并点击
        self.find_and_click(self._detail_ele)
        # 找到编辑成员并点击
        self.find_and_click(self._edit_member_ele)
        # 跳转到编辑成员页面
        return EditMemberPage(self.driver)
