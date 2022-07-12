# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_path.py
# @Time      :2022-05-02 22:29
# @Author    :DongWenFei

import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

case_dir=os.path.join(base_dir,"TestCases")#测试用例路径
# ############ #多个业务模块，多个用例文件夹，怎么处理
#TestCases创建一个上层文件夹，里面包含多个子文件夹，编写测试类

debug_dir=os.path.join(base_dir,"TestDebug")#测试用例调试路径

datas_dir=os.path.join(base_dir,"TestDatas")#测试数据路径

reports_dir=os.path.join(base_dir,"Outputs\\reports")#测试报告

report_dir = os.path.join(base_dir, "Outputs\\report")#pytest报告所在路径

logs_dir=os.path.join(base_dir,"Outputs\\logs")#日志路径

conf_dir=os.path.join(base_dir,"Conf")#配置文件路径

#print("路径输出："+datas_dir)
