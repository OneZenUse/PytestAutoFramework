# -*- coding: utf-8 -*-
'''
-------------------------------------------------
   File Name：test_002.py
   Author   : OneZen（一禅）
   Date     ：2020/8/8
-------------------------------------------------
'''
import pytest
import allure
import os

@pytest.fixture(scope='function')
def login():
    print("登录")
    yield
    print("登录完成")

@allure.feature('加入购物车！')
def test_1(login):
    '''将苹果加入购物车'''
    print("测试用例1123123123")

@allure.feature('加入购物车！')
def test_2():
    '''将橘子加入购物车'''
    print("测试用例212312312312312")
