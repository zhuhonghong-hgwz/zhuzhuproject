"""
测试用例：
1.类的实例化
2.创建标签-更新标签名字-删除标签-获取标签列表等方法调用
3.断言
"""

from test_api.api.tags import Tags
from test_api.api.wework import WeWork


class TestTags():
    #定义一个公共方法获取token
    def setup_class(self):
        #实例化获取toekn的类Work,就能调用获取token的方法了
        wework=WeWork()
        #实例化Tags类，供下面的方法调用它的方法
        self.tags=Tags()
        #实例化变量调用WeWork类的方法
        self.token=wework.get_token()
        #tagid定义为全局变量，可供其他方法调用
        self.tagid=3

    #新建标签测试用例
    def test_creat_tags(self):
        #全局变量self.tag调用Tags类中的新建标签方法,并传入token和tagid两个实参
        r=self.tags.creat_tags(self.token,self.tagid)
        #定义list变量存放获取到的tags列表值，
        list=self.tags.get_tags_list(self.token,self.tagid)
        #断言tag标签是否创建成功,业务逻辑断言
        assert list['tagname'] == '标签1'
        #单接口字段验证
        assert r['errmsg'] == 'created'

    #更新标签测试用例
    def test_update_tags(self):
        #调用更新标签方法，并传入实参
        r=self.tags.update_tags(self.token,self.tagid)
        # 定义list变量存放获取到的tags列表值，
        list = self.tags.get_tags_list(self.token, self.tagid)
        # 验证更新后数据的正确性,业务逻辑断言
        assert list['tagname'] == '更新后的标签'
        # 验证单接口字段的正确性
        assert r['errmsg'] == 'updated'

    #删除标签测试用例
    def test_delete_tags(self):
        #调用删除标签方法，并传入两个实参
        r=self.tags.delete_tags(self.token,self.tagid)
        list=self.tags.get_tags_list(self.token,self.tagid)
        # 断言tagname不在列表中，就代表删除成功了
        assert 'tagname' not in list
        # 验证单接口字段的正确性
        assert r['errmsg'] == 'deleted'


