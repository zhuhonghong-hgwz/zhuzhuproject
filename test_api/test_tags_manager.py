"""
单接口测试校验：
1.定义创建标签,更新标签，删除标签，获取标签列表方法
2.参数的实例化
"""
import pytest
import requests


class TestTags:
    # 定义一个公共初始化方法：获取token
    def setup_class(self):
        corp_id = "ww524bcb5a02101a58"
        corp_secrect = "jfF4mymhHtk-b4kb7VmJ1vrlyBCnrqaeKpFx7t2oF6Y"
        get_token_url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secrect}"
        r = requests.get(url=get_token_url)
        # 定义一个全局的变量存放获取到的token值，供下面的方法使用
        self.token = r.json()['access_token']
        # self.tag_id = 12

    # 实例化新建标签参数：
    """
    合法参数,创建成功
    必填项验证：tagname不填，提示错误信息；
    长度验证：tagname参数33位，超出长度限制，提示错误信息；
    """

    # 定义三个传入的参数：tagname，tagid和请求结果,并给定实参
    @pytest.mark.parametrize(
        'tagname,tagid,errcode',
        [("12345678901234567890123456789012", 12, 0),
         ("", 13, 40072),
         ("123456789012345678901234567890123", 14, 40058)
         ])
    def test_create_tags(self, tagname, tagid, errcode):
        # 定义创建创建标签的url
        creat_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        # 定义请求体
        data = {
            "tagname": tagname,
            "tagid": tagid
        }
        # 根据接口文档说明，创建标签使用post请求,请求体使用Json数据格式
        r = requests.post(url=creat_tags_url, json=data)
        # 打印创建结果
        print(r.json())
        # 验证接口字段的正确性
        assert r.json()['errcode'] == errcode

    # 实例化更新标签参数
    """
    合法参数,更新成功
    必填项验证：tagname不填，提示错误信息
    """

    @pytest.mark.parametrize(
        'tagid,tagname,errcode',
        [(12, '更新后的标签', 0),
         (12, '', 40072),
         ])
    # 更新标签名字
    def test_update_tags(self, tagid, tagname, errcode):
        upate_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        # 定义请求包体
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        r = requests.post(url=upate_tags_url, json=data)
        print(r.json())
        # 更新标签接口字段验证
        assert r.json()['errcode'] == errcode

    # 获取标签列表实例化
    """
        合法参数,获取列表成功
        异常验证：tagid不存在，提示错误信息           
    """

    @pytest.mark.parametrize(
        'tagid,errcode',
        [(12, 0),
         (13, 40068)
         ]
    )
    def test_tags_list(self, tagid, errcode):
        # 定义获取列表的url
        get_tags_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}"
        # 发送获取列表请求
        list = requests.get(url=get_tags_list_url)
        print(list.json())
        assert list.json()['errcode'] == errcode

    # 实例化删除标签参数
    """
    合法参数,删除成功
    异常验证：tagid不存在，提示错误信息           
    """

    @pytest.mark.parametrize(
        'tagid,errcode',
        [(12, 0),
         (13, 40068),
         ])
    # 删除标签
    def test_delete_tags(self, tagid, errcode):
        delete_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        r = requests.get(url=delete_tags_url)
        print(r.json())
        # 删除标签接口断言
        assert r.json()['errcode'] == errcode
