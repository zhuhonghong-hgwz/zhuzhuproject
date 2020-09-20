"""
单接口测试校验：获取token
"""

import pytest
import requests


class TestToken:
    # 参数化实现不同情况下获取access_token的测试
    # 定义三个参数，分别存放corpid,corpsecret和获取token的结果
    # 实参分别传入三组数据：正常的corpid和corpsecret,不传corpid,不传corpsecret
    @pytest.mark.parametrize(
        'corp_id,corp_secrect,result',
        [("ww524bcb5a02101a58", "jfF4mymhHtk-b4kb7VmJ1vrlyBCnrqaeKpFx7t2oF6Y", 'ok'),
         ("", "jfF4mymhHtk-b4kb7VmJ1vrlyBCnrqaeKpFx7t2oF6Y", 'corpid missing'),
         ("ww524bcb5a02101a58", "", 'corpsecret missing')
         ]
    )
    def test_get_token(self, corp_id, corp_secrect, result):
        get_token_url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secrect}"
        r = requests.get(url=get_token_url)
        print(r.json())
        assert r.json()['errmsg'] == result
