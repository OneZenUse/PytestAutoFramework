import os
import pytest
import allure


@pytest.fixture(scope='function')
def login():
	print("登录")
	yield
	print("登录完成")


@allure.feature('加入购物车')
def test_1(login):
	'''将苹果加入购物车'''
	print("asdasdasdasdasda")


@allure.feature('加入购物车')
def test_2():
	'''将橘子加入购物车'''
	print("tasdadadasdasdas")
