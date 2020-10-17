"""
测试用例：
添加成员并断言是否添加成功
删除联系人并断言
"""
from time import sleep

import pytest

from appium_weixin_po.pages.app import App


class TestContact:
    def setup(self):
        """
        应用的启动
        :return:
        """
        # 实例化App类，调用它的start启动方法
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        """
        关闭应用
        :return:
        """
        self.app.stop()

    # 添加成员参数化
    @pytest.mark.parametrize(
        'name, gender, phonenum',
        [('hogwarts003', '男', '13382155773'),
         ('hogwarts001', '女', '13382155774'),
         ('hogwarts', '男', '13382155763'),
         ]
    )
    def test_add_member(self, name, gender, phonenum):
        mypage = self.main.goto_addresslist().add_member().add_member_manual().edit_name(name).edit_gender(
            gender).edit_phonenum(phonenum).click_save()
        mytoast = mypage.get_toase()
        assert "添加成功" == mytoast

    # 删除成员参数化
    @pytest.mark.parametrize(
        'name',
        ['hogwarts001', 'hogwars003', 'hogwarts']
    )
    def test_delete_member(self, name):
        # 删除联系人前进入到搜索页面，输入联系人
        before_delete = self.main.goto_addresslist().goto_search_member().search_member_input(name)
        # 获取到删除之前的联系人数量
        before_num = before_delete.get_before_delete_member_list(name)
        # 没有搜索到联系人
        if before_num == 1:
            print("没有可删除的联系人")
            assert before_num == 1
        # 搜索到联系人
        else:
            # 删除联系人操作
            after_delete = before_delete.go_to_personal_info().go_to_edit_member().delete_member()
            # 获取删除联系人后的数量
            after_num = after_delete.get_after_delete_member_list(name)
            # 断言
            assert after_num == before_num - 1
