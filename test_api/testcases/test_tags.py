"""
测试用例：
1.类的实例化
2.创建标签-更新标签名字-删除标签-获取标签列表等方法调用
3.断言
"""
import yaml

from test_api.api.tags import Tags



class TestTags:
    # 定义一个公共方法获取token
    def setup_class(self):
        # #实例化获取toekn的类Work,就能调用获取token的方法了
        # wework=WeWork()
        # 实例化Tags类
        self.tags = Tags()
        config_info = yaml.safe_load(open("config.yaml"))
        #可以调用到Tags继承的父类的方法
        self.tags.get_token(config_info["token"]["corp_secret"])
        # #实例化变量调用WeWork类的方法
        # self.token=wework.get_token()
        # tagid定义为全局变量，可供其他方法调用
        self.tag_id = 3

    # 新建标签测试用例
    def test_creat_tags(self):
        # 全局变量self.tag调用Tags类中的新建标签方法,并传入tagid实参
        r = self.tags.creat_tags(self.tag_id)
        # 定义list变量存放获取到的tags列表值，
        list = self.tags.get_tags_list(self.tag_id)
        print(list)
        tag_name = self.tags.base_jsonpath(list, "$..tagname")
        assert '标签1' in tag_name
        # 断言tag标签是否创建成功,业务逻辑断言
        # assert list['tagname'] == '标签1'
        # 单接口字段验证
        assert r['errmsg'] == 'created'

    # 更新标签测试用例
    def test_update_tags(self):
        # 调用更新标签方法，并传入实参
        r = self.tags.update_tags(self.tag_id)
        # 定义list变量存放获取到的tags列表值，
        list = self.tags.get_tags_list(self.tag_id)
        print(list)
        tag_name = self.tags.base_jsonpath(list, "$..tagname")
        assert '更新后的标签' in tag_name
        # 验证更新后数据的正确性,业务逻辑断言
        #assert list['tagname'] == '更新后的标签'
        # 验证单接口字段的正确性
        assert r['errmsg'] == 'updated'

    # 删除标签测试用例
    def test_delete_tags(self):
        list1 = self.tags.get_tags_list(self.tag_id)
        print(list1)
        # 调用删除标签方法，并传入实参
        r = self.tags.delete_tags(self.tag_id)
        list2 = self.tags.get_tags_list(self.tag_id)
        print(list2)
        # tag_id = self.tags.base_jsonpath(list, "$..ta")
        assert len(list2) == len(list1)-1
        # 断言tagname不在列表中，就代表删除成功了
        # assert 'tagname' not in list
        # 验证单接口字段的正确性
        assert r['errmsg'] == 'deleted'
