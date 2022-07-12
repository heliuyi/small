# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_log.py
# @Time      :2022-05-02 22:29
# @Author    :DongWenFei

import logging,os
from Common.handle_configs import conf
from Common.handle_path import logs_dir

class MyLogger(logging.Logger):
    def __init__(self,file=None):
        #def __init__(self, name, level=logging.INFO, file=None):
        #super().__init__(name,level)#设置输出级别，输出渠道，输出日志格式
        super().__init__(conf.get("log","name"),conf.get("log","level"))
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'  # 创建一个格式器
        formatter=logging.Formatter(fmt)

        handle1=logging.StreamHandler()#控制台渠道
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:#文件渠道
            handle2=logging.FileHandler(file,encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

if conf.getboolean("log","file_ok"):#判断配置文件中路径开关是否开启
    file_name=os.path.join(logs_dir,conf.get("log","file_name"))
else:
    file_name=None#没有路径，则不写入文件

logger = MyLogger(file=file_name)

if __name__=="__main__":
    # mlogger=MyLogger("py30",file="my_log.log")
    #mlogger = MyLogger(conf.get("log", "name"), conf.get('log', "level"), file=file_name)
    mlogger = MyLogger(file=file_name)
    mlogger.info("测试，我自己封装的日志信息")

