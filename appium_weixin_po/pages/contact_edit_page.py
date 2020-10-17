"""
手动添加成员页面：添加姓名，性别，手机号，保存
"""
# from appium_weixin_po.pages.member_invite_page import MemberInvitePage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from appium_weixin_po.pages.base_page import BasePage


class ContactEditPage(BasePage):
    _member_name = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']")
    _gender_ele = (MobileBy.XPATH, "//*[@text='男']")
    _female_ele = (MobileBy.XPATH, "//*[@text='女']")
    _male_ele = (MobileBy.XPATH, "//*[@text='男']")
    _phone_num_ele = (MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    _save_ele = (MobileBy.ID, "com.tencent.wework:id/hvk")
    # 定义一个构造函数接收传递过来的drivr
    # def __init__(self, driver):
    #     self.driver = driver

    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find_and_send_keys(self._member_name, name)
        # 添加姓名后停留在当前页面，所以return self
        return self

    def edit_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.find_and_click(self._gender_ele)
        if gender == "女":
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click(self._female_ele)
        else:
            sleep(3)
            # element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
            # element.click()
            self.find_and_click(self._male_ele)
        return self

    def edit_phonenum(self, phonenum):
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']").send_keys(phonenum)
        self.find_and_send_keys(self._phone_num_ele, phonenum)
        return self


    def click_save(self):
        # 点击保存后跳转到添加成员方式选择页面
        from appium_weixin_po.pages.member_invite_page import MemberInvitePage
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hvk").click()
        self.find_and_click(self._save_ele)
        return MemberInvitePage(self.driver)

