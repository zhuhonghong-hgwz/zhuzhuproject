"""
添加部门测试用例
"""
import pytest

from weixin_selenium_po.pages.basepage import BasePage
from weixin_selenium_po.pages.main_page import MainPage


class TestCreateDepartment:
    # 执行用例前先初始化首页
    def setup(self):
        # 实例化Main页面，可以调用MainPage中的方法
        self.main = MainPage()

    #添加成功的部门数据参数化：
    #参数最小长度验证：1个字符
    #参数最大长度验证：32个字符
    #参数类型验证：字母+数字+中文+特殊字符
    @pytest.mark.parametrize(
        'depart_name',
        ['1',
         'abc@123部门',
         '12345678901234567890123456789012'
        ]
    )
    #成功添加部门测试用例
    def test_create_department(self, depart_name):
        # 调用页面对象中各方法实现添加部门:通讯录页面的添加部门页面，添加部门，点击确认保存部门，获取部门列表
        depart_list = self.main.go_to_contact().go_to_create_department().create_department(depart_name).save_department().get_department_list()
        print(depart_list)
        # 断言部门是否添加成功
        assert depart_name in depart_list

    # 添加失败的部门数据参数化：
    # 数据长度验证：33个字符
    # 数据类型验证：数据中包含不支持的字符\:?”<>｜(此处有bug)
    @pytest.mark.parametrize(
        'depart_name',
        ['123456789012345678901234567890123',
         '\:?”<>｜'
         ]
    )
    # 添加部门失败测试用例
    def test_create_department_fail(self, depart_name):
        depart_list = self.main.go_to_contact().go_to_create_department().create_department(depart_name).save_department().get_department_list()
        print(depart_list)
        assert depart_name not in depart_list

    #资源回收
    def teardown(self):
       self.main.driver.quit()
