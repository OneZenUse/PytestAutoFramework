# -*- coding: utf-8 -*-

'''----------------------------------------------
   FileName： test_003
   Author:    OneZen
   Date：     2020/9/22
----------------------------------------------'''
import allure
import pytest
import requests
from test_Config import Config
from test_Common import Assertions

#host = Config.Config.VALUE_HOST
host ='http://161.113.124.202:15269/assets/product/flow/list'

@pytest.fixture(scope='function')
def login():
    print("登录")
    yield
    print("登录完成")

@allure.feature('测试登录操作！')
def test_login1():
        url = host
        data = {
            "companyId": "",
            "demandBeginTime": "",
            "demandEndTime": "",
            "key": "",
            "page": 0,
            "signBeginTime": "",
            "signEndTime": "",
            "size": 0,
            "type": "",
            "typeId": 0,
            "userId": ""
        }
        r = requests.post(url, data=data)
        print("返回结果:%s" %r.text)

        # 实际返回结果
        result_reason = r.json().get("msg")
        result_error_code = r.json().get("code")

        # 断言接口
        Assertions.Assertions.assert_code = result_error_code == "500"

        assert result_reason == "系统繁忙，请稍后再试。"
        #assert "data"== "PARAM_MISS"
