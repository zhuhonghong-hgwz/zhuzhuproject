"""
具体业务：创建标签-更新标签名字-删除标签-获取标签列表
"""


from test_api.api.wework import WeWork

#继承WeWork可以直接使用父类的属性token
class Tags(WeWork):
    # 定义新建标签方法，并传入形参：tagid
    def creat_tags(self, tag_id):
        # 定义创建创建标签的url
        # creat_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        # 定义请求体
        data = {
            "tagname": "标签1",
            "tagid": tag_id
        }
        # 根据接口文档说明，创建标签使用post请求,请求体使用Json数据格式
        # r = requests.post(url=creat_tags_url, json=data)
        req={
            "method":"post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}",
            "json":data
        }
        r = self.base_requests(req)
        # return json格式的返回体
        return r.json()

    # 定义更新标签方法，并传入形参：tagid
    def update_tags(self, tag_id):
        # upate_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        # 定义请求包体
        data = {
            "tagid": tag_id,
            "tagname": "更新后的标签"
        }
        # r = requests.post(url=upate_tags_url, json=data)
        req={
            "method":"post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}",
            "json":data
        }
        r = self.base_requests(req)
        # return json格式的返回体
        return r.json()

    # 定义删除标签方法，并传入形参：tagid
    def delete_tags(self,tag_id):
        # delete_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        # r = requests.get(url=delete_tags_url)
        req={
            "method":"get",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        }
        r = self.base_requests(req)
        print(r.json())
        # return json格式的返回体
        return r.json()

    #定义获取标签列表的方法，并传入形参tagid
    def get_tags_list(self, tag_id):
        # 定义获取列表的url
        # get_tags_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tag_id}"
        # 发送获取列表请求
        # list = requests.get(url=get_tags_list_url)
        req={
            "method":"get",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tag_id}"
        }
        r = self.base_requests(req)
        return r.json()
