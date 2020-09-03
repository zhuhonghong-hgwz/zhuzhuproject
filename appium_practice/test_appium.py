from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

#企业微信测试
class TestWeixin:
    # setup中存放初始化信息
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        #缩短动态页面的等待时间
        caps['settings[waitForIdleTimeout]'] = 0
        # 不请空缓存，用于记住上一次的弹框或登录等信息
        caps["noReset"] = "True"
        # 客户端与appium server端建立连接，同时打开欢迎页appActivity
        self.driver = webdriver.Remote("http://127。0.0.1:4723/wd/hub", caps)
        # 隐式等待，增加查找元素时的稳定性
        self.driver.implicitly_wait(5)

    # 释放资源
    def teardowm(self):
        self.driver.quit()

    def test_daka(self):
        """
        微信打卡功能
        :return:
        """
        # 找到工作台并点击
        el1 = self.driver.find_element_by_xpath('//*[@text="工作台"]').click()
        # 滑动找到打卡并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        # 找到外出打卡并点击
        el3 = self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()
        # 点击进行打卡
        el4 = self.driver.find_element_by_xpath('//*[contains(@text, "次外出")]').click()
        # 找到打卡成功后的页面元素
        ele = self.driver.find_element_by_id("com.tencent.wework:id/oh")
        # 加断言，判断查找到的文本信息是不是”外出打卡成功“
        assert "外出打卡成功" == ele.text

