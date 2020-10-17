"""
搜索联系人页面:
输入联系人
获取搜索到的联系人数量
跳转到个人信息页面
获取删除联系人后查询到的数量
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from appium_weixin_po.pages.base_page import BasePage
from appium_weixin_po.pages.personal_info_page import PersonalInfoPage


class SearchMemberPage(BasePage):
    _input_ele = (MobileBy.ID, "com.tencent.wework:id/gfs")
    #_wait_beforenum_ele = (MobileBy.XPATH, "//*[@text='联系人']")
    #_wait_afternum_ele = (MobileBy.XPATH, "//*[@text='联系人']")

    #输入联系人
    def search_member_input(self, name):
        # 查找到搜索框，并输入查询的相关信息
        self.find_and_send_keys(self._input_ele, name)
        #如果搜索不到联系人，不会出现等待的元素，会出现等待超时
        # 显示等待查询的元素出现
        #self.wait(self._wait_beforenum_ele)
        sleep(3)
        #停留在当前页面
        return self

    #获取删除联系人前搜索到的数量
    def get_before_delete_member_list(self, name):
        # 查找当前页面与搜索内容相关的元素
        self.eles = self.finds(name)
        # # 定义一个变量用于存放查找到的元素个数
        self.beforenum = len(self.eles)
        return self.beforenum

    # 点击搜索到的姓名跳转到个人信息页面
    def go_to_personal_info(self):
        # 如果数量小于于2，说明没有查找到联系人，打印提示信息，结束操作
        if self.beforenum < 2:
            #返回查找到的数量，用于做判断
            return self.beforenum
        else:
            # 如果数量小于于2，说明有查找到联系人，则点击查找到的第一个元素，进入到个人信息页面
            self.eles[1].click()
            return PersonalInfoPage(self.driver)

    #获取删除联系人后的成员列表
    def get_after_delete_member_list(self, name):
        # 如果搜索不到联系人，不会出现等待的元素，会出现等待超时
        # 显示等待查询的元素出现
        # self.wait(self._wait_afternum_ele)
        sleep(3)
        # 再次搜索当页的text文本与搜索内容相关的数量
        eles = self.finds(name)
        # 定义变量afternum存放本次查找到的联系人数量
        afternum = len(eles)
        return afternum
