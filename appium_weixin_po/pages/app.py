"""
存放app端特有操作：
启动app,关闭app,重启app,进入首页
"""
from appium import webdriver

from appium_weixin_po.pages.base_page import BasePage
from appium_weixin_po.pages.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            # 不请空缓存，用于记住上一次的弹框或登录等信息
            caps["noReset"] = "True"
            # 客户端与appium server端建立连接，同时打开手机app端首页
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            #start_activity需要传入app_package和app_activity，可用于启用其他的应用
            #self.driver.start_activity(appPackage,appActivity)
            #launch_app不需要传入任何参数,启动desirecap里面设置的appActivity
            self.driver.launch_app()
        # 隐式等待，增加查找元素时的稳定性
        self.driver.implicitly_wait(5)
        return self


    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    #->标记返回值数据类型
    def goto_main(self)->MainPage:
        return MainPage(self.driver)
