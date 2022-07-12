# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_data.py
# @Time      :2022-05-02 22:29
# @Author    :DongWenFei

import re
from Common.handle_configs import conf

#1.一条用例涉及到数据当中，有url,request_data,check_sql
class EnvData:
    '''
    存储用例要使用到的数据(上一个接口的返回值存储到*类属性*中做为一个全局变量)
    全面支持业务流程
    下一个接口的请求依赖于上一个接口的请求返回值
    思想：提取上一个接口的返回值，然后设置为全局变量，下一个接口调用这个全局变量就好了
    '''
    pass

def replace_mark_with_data(case,mark,real_data):
    '''
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    :param case:excel当中读取出来一条数据。是个字典
    :param mark:数据当中的占位符。#值#
    :param real_data:要替换mark的真实数据
    :return:
    '''
    for key,value in case.items():
        #确保是个字符串
        if value is not None and isinstance(value,str):
            if value.find(mark)!=-1:#找到标识符
                case[key]=value.replace(mark,real_data)
    return case

def replace_mark_with_data_int(case,mark,real_data):
    '''
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    :param case:excel当中读取出来一条数据。是个字典
    :param mark:数据当中的占位符。#值#
    :param real_data:要替换mark的真实数据
    :return:
    '''
    for key,value in case.items():
        #确保是个字符串
        if value is not None and isinstance(value,str):

            if value.find(mark)!=-1:#找到标识符
                result=value.replace(mark,real_data)
                #print("==========替换前的的{}===========".format(result))
                result = re.sub('"', "", result)#除去字符串中的双引号
                #print("==========替换后的{}===========".format(result))
                case[key]=result
    return case
# --------------升级版  替换数据同时可以去找测试类和配置文件中的数据--------------------
def replace_data(data, cls):
    """
    替换数据
    :param data: 要进行替换的用例数据(字符串)
    :param cls: 测试类
    :return:
    """
    while re.search('#(.+?)#', data):
        res2 = re.search('#(.+?)#', data)
        item = res2.group()
        attr = res2.group(1)
        try:
            value = getattr(cls, attr)
        except AttributeError:
            value = conf.get('test_data',attr)
        # 进行替换
        data = data.replace(item, str(value))
    return data



if __name__ == '__main__':
    pass
    cases={'case_id': 1, 'title': '秒杀活动详情', 'method': 'get', 'url': 'promote/secKill/detail?activityId="#activityId#"', 'request_data': None, 'expected': '{\n  "code": 0,\n  "msg": null,\n  "success": true\n}', 'check_sql': None}
    result=replace_mark_with_data_int(cases,'#activityId#','9090')
    print(result)


    # if case["request_data"].find("#phone#") != -1:
    #     new_phone = get_new_phone()  # 字符串查找-替换-赋值
    #     #case=replace_mark_with_data(case, "#phone#", new_phone)
    #     case=replace_data(case['request_data'])
    #     print(case)
    # for key,vlaue in case.items():
    #     print(key,vlaue)

