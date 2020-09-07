from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


# 定义一个方法读取yml文件数据
def get_datas():
    with open("./datas/catact.yml", encoding='utf-8') as f:
        contactdatas = yaml.safe_load(f)
        # 获取添加联系人数据
        adddatas = contactdatas["add_datas"]
        # 获取删除联系人数据
        deldatas = contactdatas["del_datas"]
    return adddatas, deldatas


# 微信测试类
class TestWeixinContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        # 不请空缓存，用于记住上一次的弹框或登录等信息
        caps["noReset"] = "True"
        # 客户端与appium server端建立连接，同时打开手机app端首页
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 隐式等待，增加查找元素时的稳定性
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 增加微信联系人的参数化数据
    @pytest.mark.parametrize('name,gender,phonenum', get_datas()[0])
    # 增加微信联系人测试用例
    def test_addcontract(self, name, gender, phonenum):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='男']"))
            element.click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']").send_keys(
            phonenum)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hvk").click()
        # WebDriverWait()until()方法等待toast出现
        mytoast = WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        # Toa出现后才能获取到它的文本信息并进行判断
        assert "添加成功" == mytoast.text

    # 删除微信联系人的参数化数据
    @pytest.mark.parametrize('name', get_datas()[1])
    # 删除微信联系人,只适合联系人少，在当前页面删除的情况
    def test_deletecontact(self, name):
        # 找到通讯录并点击
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        # 滑动查找需要删除的联系人姓名,并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{name}").instance(0));').click()
        # 找到右上角的三个点并点击
        self.driver.find_element_by_id("com.tencent.wework:id/hvd").click()
        # 找到编辑成员并点击
        self.driver.find_element_by_id("com.tencent.wework:id/b87").click()
        # 滑动到下面找到删除成员按钮，并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        # 点击提示框中的确认按钮，确认删除
        self.driver.find_element_by_id("com.tencent.wework:id/bit").click()

        # 查找元素时找不到，加入显示等待,直到能找到创建人元素时才进行下一步操作
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.ID, "com.tencent.wework:id/b8p"))
        # find_elements查找删除联系人后页面中Text信息
        contact_ele = self.driver.find_elements_by_xpath(
            "//*[@resource-id='com.tencent.wework:id/i2b']//*[@class='android.widget.TextView']")
        # 定义一个列表用于存放所有联系人
        contact_list = []
        # for循环将查找到的Text信息存放到列表中
        for name1 in contact_ele:
            contact_list.append(name1.text)
        # 用于查看删除联系人后的列表信息
        print(contact_list)
        # 点击删除后联系人过一会才会消失，所以需要设置等待,直到找不到删除的联系人后再进行断言
        WebDriverWait(self.driver, 10).until_not(lambda x: x.find_element(MobileBy.XPATH, "//*[@text=name]"))
        # 判断联系人是否成功删除
        assert name not in contact_list

    # 删除微信联系人的参数化数据
    @pytest.mark.parametrize('name', get_datas()[1])
    # 搜索联系人删除，适合联系人多的情况
    def test_search_delcontact(self,name):
        # 找到通讯录并点击
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        # 查找右上角搜索按钮，并点击
        self.driver.find_element_by_id("com.tencent.wework:id/hvn").click()
        # 查找到搜索框，并输入查询的相关信息
        self.driver.find_element_by_id("com.tencent.wework:id/gfs").send_keys(name)
        # 显示等待查询的元素出现
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='联系人']"))
        # 搜索当页的text文本与ez相关的元素
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        # 定义一个变量用于存放查找到的元素个数
        beforenum = len(eles)
        # 查看元素个数
        print(beforenum)
        # 如果数量大于2，说明有查找到联系人，则点击第一个元素并进行后续的删除操作
        if beforenum > 2:
            eles[1].click()
            # 找到右上角的三个点并点击
            self.driver.find_element_by_id("com.tencent.wework:id/hvd").click()
            # 找到编辑成员并点击
            self.driver.find_element_by_id("com.tencent.wework:id/b87").click()
            # 滑动到下面找到删除成员按钮，并点击
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector()'
                                     '.scrollable(true).instance(0))'
                                     '.scrollIntoView(new UiSelector()'
                                     '.text("删除成员").instance(0));').click()
            # 点击提示框中的确认按钮，确认删除
            self.driver.find_element_by_id("com.tencent.wework:id/bit").click()
            # 显示等待查询的元素出现
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='联系人']"))
            # 再次搜索当页的text文本与ez相关的数量
            result_eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
            # 定义变量afternum存放本次查找到的联系人数量
            afternum = len(result_eles)
            # 查看删除联系人后的元素个数
            print(afternum)
            # 断言再次查找到的元素个数比原来查找到的少一个，则删除成功
            assert afternum == beforenum - 1

