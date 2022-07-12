# *_* coding : UTF-8 *_*

# 开发时间  ：  2022/6/22  15:27
# 文件名称  :  run.PY
# 开发工具  :  PyCharm

# import unittest
# from BeautifulReport import BeautifulReport
# from Common.handle_path import case_dir,reports_dir
#
# s=unittest.TestLoader().discover(case_dir)
# br=BeautifulReport(s)
# br.report("接口自动化测试",'report.html',reports_dir)

import unittest
from unittestreport import TestRunner
from Common.handle_path import case_dir,reports_dir

suite1 = unittest.defaultTestLoader.discover(case_dir)

runner = TestRunner(suite=suite1,
                 filename="report01.html",
                 report_dir=reports_dir,
                 title='接口自动化测试报告',
                 tester='Test',
                 desc="接口自动化测试报告",
                 templates=2)  #1 2
runner.run()

# #########################测试结果推送到钉钉群组#################################
# webhook = 'https://oapi.dingtalk.com/robot/send?access_token=362b478a12125d202ecb95037fdab29c130bd80c32b59'
# runner.dingtalk_notice(url=webhook,key='测试')