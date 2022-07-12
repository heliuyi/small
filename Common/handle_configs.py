# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_configs.py
# @Time      :2022-05-02 22:29
# @Author    :DongWenFei

from configparser import ConfigParser
import os
from Common.handle_path import conf_dir
class HandleConfig(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")

file_path=os.path.join(conf_dir,'small.ini')
conf=HandleConfig(file_path)#读取配置文件中的数据

if __name__ == '__main__':
    pass
#     print(file_path)
#     conf=HandleConfig(file_path)
#     result=conf.get("log",'file_ok')
#     print(result)
