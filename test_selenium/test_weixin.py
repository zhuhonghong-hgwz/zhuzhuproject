import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeixin:
    def setup(self):
        # 实现复用浏览器
        # 实例化Options类，再作为参数传入webdriver.Chrome中
        # option = Options()  # 导入chrome的Options
        # option.debugger_address = '127.0.0.1:9223'
        # self.driver = webdriver.Chrome(options=option)
        # 初始化浏览器
        self.driver = webdriver.Chrome()
        # 隐式等待5s
        self.driver.implicitly_wait(5)
        # 窗口最大化
        self.driver.maximize_window()

    def teardown(self):
        # 关闭浏览器
        self.driver.quit()

    def test_importcotact(self):

        # 获取当前页面cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # #打开index页面，需要登录
        #self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #
        # cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853782152932'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'DjZOG_FwnEBBw_zCb3r643Cylag3m490kU2Gh5skRHQvwITPp7Pkwn-rRcVee18hWbW34m7qhPJVfkVZX7IBFqkTsrYnCO9Hrmf1VrI1n84R8QI-SlNiqgWCPMSpSn9-Li0o08eLn3mTBSuL4fxbwj3NGsmxKpfDpx5CYGOqbrL-8dPD8jWI30K72pq7-JTotO7J5AEHLegKEQhBmqW5a2wsnqET3I26OYDjIIKp87Rb1jbBSI_FHk-wfCjYL2QBLOLZdGIfTrXVLRET3w73rQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853782152932'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325020156592'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'UXNVbP9e8rCrk2U7-13acqqttX11wqKGtJd_6O5VSmF6kU-blpXVuCQV2-x04JkN'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3115551'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '3197154360'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629646440, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598108810,1598110064,1598110265,1598110440'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598110440'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '10593773352036888'}, {'domain': '.qq.com', 'expiry': 1598196854, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1395252612.1598021475'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598137100, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '6i692r8'}, {'domain': '.qq.com', 'expiry': 1661182454, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1868196983.1597886112'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629422110, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600702457, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-tw%2Ccht'}]
        #cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853782152932'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '_Sjnc0cUq_z8Kc--lJDVjAaNgEFPBqeM0S6Xo7nf2zXfy0-_kFpBbCDFmMGxHfeUFsSAK6ENWxTf-kI-YwZPnz4XQq7xEWd1acNdQ8FfcaA4aezpIvcppdab1nPwX657PRvkdEqwnEAFWd9amcwo-c_MeotDD0u9Dc_shSmQyswLdzRQf3G0WG1ZkCTkQJ0hXAM1p_kUJkh963NCoaiBMLh6S5opckFJQqolfJ_CIt0CEctIYHUDnr5gkdv5Kpf_aRjuqB3i8eFAcQEOoPP9uA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853782152932'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325020156592'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'UXNVbP9e8rCrk2U7-13acvxqj-SmqIyvCX5To9GyGXPeeUnzm_ucP44dIeo5FAaQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9065189'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '3197154360'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629689071, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598110064,1598110265,1598110440,1598153072'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598153072'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '10593773351470796'}, {'domain': '.qq.com', 'expiry': 1598239492, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1395252612.1598021475'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598184607, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '6pqp3aj'}, {'domain': '.qq.com', 'expiry': 1661225092, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1868196983.1597886112'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629422110, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600745216, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-tw%2Ccht'}]

        #shelve创建一个小型数据库，并打开
        db=shelve.open('./mydbs/cookies')
        #将cookies存放在key为cookie的数据库中
        # db['cookie']=cookies
        # #存储完成后关闭数据库
        # db.close()
        #从shelve数据库中获取cookies
        cookies=db['cookie']
        #打开尚未添加cookies的index页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # # 往当前页面添加cookies
        for cookie in cookies:
            # 加入判断，如果有expiry就删除
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # add_cookie中传入的是字典形式的数据
            self.driver.add_cookie(cookie)
        # 重新打开已带有cookie信息的index页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #sleep(3)
        # 打开‘导入通讯录’，点击文件上传，并判断上传的文件格式是否正确
        # 先定位到元素‘导入通讯录’,并点击
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # 确认id唯一，通过id定位到元素‘上传文件’
        self.driver.find_element_by_id("js_upload_file_input").send_keys("C:/Users/15895/Desktop/mydata.xlsx")
        # 文件上传后定位到上传后的文件名称,获取它的文本信息。最后判断和我们要上传的文件名称是否一致
        assert "mydata.xlsx" == self.driver.find_element_by_id("upload_file_name").text
        sleep(3)