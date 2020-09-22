# -*- coding: utf-8 -*-
'''----------------------------------------------
   File Name：Report.py
   Author   : OneZen（一禅）
   Date     ：2020/8/8
----------------------------------------------'''

'''封装 Allure 报告方法'''

import os
import pytest

def run_case_main():
    # 执行用例
    # --reruns:失败重复执行多少次
    args = ['--alluredir', './allure-results']  # 通过allure生成json  REPORT_DIR：测试结果数据所在目录
    pytest.main(args)
    #pytest.main(['-s', '-q', '--alluredir', './report/xml'])
    # 生成html allure generate 测试结果数据所在目录 -o 测试报告保存的目录 --clean
    os.system('allure generate  ./allure-results -o ./allure-reports --clean')
