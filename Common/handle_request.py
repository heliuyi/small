# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :handle_request.py
# @Time      :2022-05-02 22:29
# @Author    :DongWenFei

import requests, json
from Common.handle_log import logger
from Common.handle_configs import conf

def send_requests(method, url, data=None, token="7298b905-2dca-460f-bb39-2e08a1d6100a"):
    '''
    :param method:
    :param url:
    :param data:字典形式的数据
    :param token:
    :return:
    '''
    logger.info("===============发起一次HTTP请求===============")
    headers = __handle_header(token)  # 得到请求头 私有化
    url = __pre_url(url)  # 得到完整的url-拼接url
    data = __pre_data(data)  # 请求数据的处理(strToJson)
    logger.info("请求头为：{}".format(headers))
    logger.info("请求方法为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(data))

    # 根据请求类型，调用请求方法
    if method.upper() == "GET":
        resp = requests.get(url, params=data, headers=headers)
    elif method.upper() == "POST":
        resp = requests.post(url, json=data, headers=headers)
    elif method.upper() == "PUT":
        resp = requests.put(url, json=data, headers=headers)
    elif method.upper() == "DELETE":
        resp = requests.delete(url, json=data, headers=headers)
    else:
        resp = requests.patch(url, json=data, headers=headers)
    logger.info("响应数据为：{}".format(resp.json()))
    return resp

def __handle_header(token=None):
    '''
    处理请求头，加上项目当中必带的请求头
    如果有token，加上token
    :param token:token值
    :return:处理之后headers字典
    '''
    # headers = {"X-Lemonban-Media-Type": 'lemonban.v2',
    #            "Content-Type": "application/json"
    #            }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
    }

    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers

    # headers = {
    #         "Accept": "application/json, text/plain, */*",
    #         "Authorization": "Basic bWlkc3RyYWdlOm1pZHN0cmFnZQ==",
    #         "Connection": "keep-alive",
    #         "Cookie": "PHPSESSID=ammjhs1eptc1u14en746oc2t20; JSESSIONID=E4A5F8950F33709D46FB40DA7B6E1049",
    #         "isToken": "false"
    # }
    #return headers

def __pre_url(url):
    '''
    拼接接口的url地址
    :param url:
    :return:
    '''
    base_url = conf.get("server", 'base_url')
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + '/' + url

def __pre_data(data):
    '''
    如果data是字符串，则转换成字典对象
    :param data:
    :return:
    '''
    if data is not None and isinstance(data, str):
        return json.loads(data)
    return data

if __name__ == '__main__':
    # urldl = "http://console.zwztf.net:9011/api/goods/whitegoods/"
    # datas = {
    #     "id": "746734823812472834",
    #     'status': 0
    # }
    # res=send_requests("put",urldl,datas)
    # print(res.json())

    pass
    # #urldl = "http://api.lemonban.com/futureloan/member/login"
    # urldl = "/member/login"
    # datas = {
    #     "mobile_phone": "15530012799",
    #     'pwd': '123456789'
    # }
    # res=send_requests("post",urldl,datas)
    # token = res.json()['data']['token_info']['token']
    # member_id = res.json()['data']['id']

    # token=jsonpath.jsonpath(res.json(), "$.data.token_info.token")[0]
    # print(token)


    # recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    # recharge_data = {'member_id': member_id, 'amount': 2000}
    # recharge_result = send_requests("POST", recharge_url, data=recharge_data, token=token)
    # print(recharge_result.json()['data'])
    # #{'id': 123587474, 'leave_amount': 16000.0, 'mobile_phone': '18202162273', 'reg_name': '小柠檬', 'reg_time': '2021-08-14 16:23:36.0', 'type': 1}

    # login_url = "/api/auth/oauth/token"
    # login_data = {
    #                 "username":"18202162273",
    #                 "password":"zV87dxG59ZepAXIV7FLJ1g==",
    #                 "randomStr":"blockPuzzle",
    #                 "code":"hmckcZ+5jLuDyeQPjHmN6XWQLmhwKgjkc57eOWOvUq22U8mjQQKbHVJpXWPGqrIsUT0H6LoVuglSlCrx//yZqQ==",
    #                 "grant_type":"password",
    #                 "scope":"server"
    #             }
    # login_result = send_requests("POST", login_url, data=login_data)
    # print(login_result.json())
