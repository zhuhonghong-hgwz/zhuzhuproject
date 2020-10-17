"""
编辑成员页面：
删除成员,返回搜索删除联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy

from appium_weixin_po.pages.base_page import BasePage


class EditMemberPage(BasePage):
    _delete_member_text = "删除成员"
    _commit_delete_ele = (MobileBy.ID, "com.tencent.wework:id/bit")

    def delete_member(self):
        # 滑动到下面找到删除成员按钮，并点击
        self.find_by_scroll_and_click(self._delete_member_text)
        # 点击提示框中的确认按钮，确认删除
        self.find_and_click(self._commit_delete_ele)
        from appium_weixin_po.pages.search_member_page import SearchMemberPage
        # 返回输入删除联系人信息页面
        return SearchMemberPage(self.driver)




