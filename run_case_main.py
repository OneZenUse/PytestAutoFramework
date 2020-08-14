from test_Common import Log
from test_Common import Email
from test_Config import Config
from test_Common.Report import run_case_main

if __name__ == '__main__':
    # 读取Config 配置信息
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

# 运行 测试用例，生成报告
try:
    run_case_main()
except Exception:
    log.error('执行用例失败，请检查环境配置')
    raise

# 发送测试报告邮件
try:
    mail = Email.SendMail()
    mail.sendMail()
except Exception as e:
    log.error('发送邮件失败，请检查邮件配置')
    raise
