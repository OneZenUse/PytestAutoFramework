# -*- coding: utf-8 -*-
'''----------------------------------------------
   File Name：Define_data.py
   Author   : OneZen（一禅）
   Date     ：2020/8/8
----------------------------------------------'''

'''定义所有测试数据'''
import os
from test_Data import Yaml_data
from test_Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = Yaml_data.GetPages().get_page_list()
    param = data[name]
    return param
'''
class Basic:
    log.info('解析yaml, Path:' + path_dir + '/test_Data/yamlDB/Basic.yaml')
    params = get_parameter('Basic')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
'''
class OrderId:
    log.info('解析yaml, Path:' + path_dir + '/test_Data/yamlDB/Orderid.yml')
    params = get_parameter('Orderid')
    url = []
    data = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
#
# class Collections:
#     log.info('解析yaml, Path:' + path_dir + '//test_Data/yamlDB/Collections.yaml')
#     params = get_parameter('Collections')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])


# class Personal:
#     log.info('解析yaml, Path:' + path_dir + '/test_Data/yamlDB/Personal.yaml')
#     params = get_parameter('Personal')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])

#
# class Login:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Login.yaml')
#     params = get_parameter('Login')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])