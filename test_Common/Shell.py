# -*- coding: utf-8 -*-
'''----------------------------------------------
   File Name：Shell.py
   Author   : OneZen（一禅）
   Date     ：2020/8/8
----------------------------------------------'''

'''封装执行 Shell 语句方法'''

import subprocess

class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o