"""
业务场景相关：创建标签-更新标签名字-删除标签-获取标签列表
"""
import requests
from jsonpath import jsonpath


class TestTags:
    # 定义一个公共初始化方法：获取token
    def setup_class(self):
        corp_id = "ww524bcb5a02101a58"
        corp_secrect = "jfF4mymhHtk-b4kb7VmJ1vrlyBCnrqaeKpFx7t2oF6Y"
        get_token_url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secrect}"
        r = requests.get(url=get_token_url)
        # 定义一个全局的变量存放获取到的token值，供下面的方法使用
        self.token = r.json()['access_token']
        self.tag_id = 12

    # 创建标签
    def test_creat_tags(self):
        # 定义创建创建标签的url
        creat_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        # 定义请求体
        data = {
            "tagname": "标签1",
            "tagid": self.tag_id
        }
        # 根据接口文档说明，创建标签使用post请求,请求体使用Json数据格式
        r = requests.post(url=creat_tags_url, json=data)
        # 打印创建结果
        print(r.json())
        # 定义获取列表的url
        get_tags_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={self.tag_id}"
        # 发送获取列表请求
        list = requests.get(url=get_tags_list_url)
        # 打印获取到的标签列表
        print(list.json())
        # 验证业务流程的正确性
        assert list.json()['tagname'] == '标签1'

    # 更新标签名字
    def test_update_tags(self):
        upate_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        # 定义请求包体
        data = {
            "tagid": self.tag_id,
            "tagname": "更新后的标签"
        }
        r = requests.post(url=upate_tags_url, json=data)
        # 打印更新后的字段信息
        print(r.json())
        # 定义获取列表的url
        get_tags_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={self.tag_id}"
        # 发送获取列表请求
        list = requests.get(url=get_tags_list_url)
        # 打印获取到的标签列表
        print(list.json())
        # 验证更新后数据的正确性
        assert list.json()['tagname'] == '更新后的标签'

    # 删除标签
    def test_delete_tags(self):
        delete_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={self.tag_id}"
        r = requests.get(url=delete_tags_url)
        print(r.json())
        # 定义获取列表的url
        get_tags_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={self.tag_id}"
        # 发送获取列表请求
        list = requests.get(url=get_tags_list_url)
        # 断言tagname不在列表中，就代表删除成功了
        assert 'tagname' not in list.json()


