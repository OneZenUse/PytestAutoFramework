# PytestAutomate 框架介绍
  
　　PytestAutoFreamwork 接口自动化测试框架，是基于Python语言加Pytest基础框架，经过二次开发设计出来的。

　　为了有效的展示报告的可读性与效率，本框架放弃了原有的 HTMLTestRunner ，采用了Allure 报告，显示更直接更美观。

#### PytestAutoFreamwork 框架主要目录介绍
* .pytest_log       日志信息目录
* allure-reports    生成HTML，Allure报告目录
* allure-results    生成XML，用例结果目录
* test_Case         测试用例编写目录
* test_Common       存放常用公共方法与代码目录
* test_Config       测试配置信息目录
* test_Data         读取/存放测试数据目录
* run_case_main.py  运行测试用例主方法 

Windows and Mac Install 
---


Issue Solution 
---

http://note.youdao.com/noteshare?id=cd6ab7fd8548b7f29a1e702c5a7e26d4&sub=DEFEE85C6531450AA5DE7FC4346F7832

---
更新说明 v 1.1.0
1. 新增安装文档
2. 新增问题解决方案文档
3. 删除 Shell 封装封装 使用os库调用 shell、cmd命令
---
更新说明 v 1.0.0
1. 重新定义 Pytest 框架
2. 封装常用测试使用的三方库（Requests、Logs、Shell……）
3. 放弃 HTMLTestRunner 报告，采用 Allure 报告
